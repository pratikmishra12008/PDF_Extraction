import re
import json
from tika import parser
parsed = parser.from_file('BHorneDATA-CAQH.PDF')
content=str(parsed["content"])
dict={
    'Last Attestation Date':re.search('Last Reattestation Date:(.*)',content).group(1).strip()[:-11], #Page 1 - Top section
    'Provider Type':re.search('Provider Type:(.*)Practice Setting',content).group(1).strip(), #Page 1 - Top section
    'First Name':re.search('First Name :(.*)Middle Name',content).group(1).strip(), #Page 1 Personal Information
    'Last Name':re.search('Last Name :(.*)Suffix',content).group(1).strip(), #Page 1 Personal Information
    'Gender':re.search('Gender :(.*)Race/Ethnicity',content).group(1).strip(), #Page 1 Personal Information
    'CAQH Provider ID':re.search('CAQH Provider ID :(.*)\n',content).group(1).strip(), #Page 1 Personal Information
    'Clincian\'s Email':re.search('Primary E­mail Address :(.*)Personal E­Mail Address :',content).group(1).strip(), #Page 1 Personal Information
    'SSN':("-").join(re.findall('\d+',re.search('Social Security Number :(.*)\n',content).group(1).strip())), #Page 1 Personal Information
    'NPI Number':re.search('Individual NPI :(.*)\n',content).group(1).strip(), #Page 1 Personal Information
    'Date of Birth':re.search('Birth Date :(.*)Birth City',content).group(1).strip(), #Page 1 Personal Information
    'Credentialing Contact Name':re.search('/Practice Name :(.*)\n',content).group(1).strip(), #Page 3 Practice locations
    'Credentialing Contact Address':re.search('CAQH Practice Location Number :(.*)\n\n(.*)\nStreet 1 :(.*)\n\nStreet 2 :(.*)Country :',content).group(3).strip(), #Page 3 Practice locations
    'Credentialing Contact City':re.search('City :(.*)State :',content).group(1).strip(), #Page 3 Practice locations
    'Credentialing Contact State':re.search('State :(.*)\n',content).group(1).strip(), #Page 3 Practice locations
    'Credentialing Contact Zip code':("-").join(re.findall('\d+',re.search('Zip Code :(.*)Email',content).group(1).strip())), #Page 3 Practice locations
    'Credentialing Contact Phone':("-").join(re.findall('\d+',re.search('Office Phone Number : (.*)Phone Extention :',content).group(1).strip())), #Page 3 Practice locations
    'Credentialing Contact Email':re.search('Zip Code :(.*)Email Address :(.*)',content).group(2).strip(), #Page 3 Practice locations
    'Licence Location State':re.search('License State :(.*)Do you currently practice',content).group(1).strip(), #Page 1 Professional Identification numbers
    'License':re.search('License Number :(.*)License',content).group(1).strip(), #Page 1 Professional Identification numbers
    'License Issue Date':re.search('License Status :(.*)\nIssue Date :(.*)Expiration Date',content).group(2).strip(), #Page 1 Professional Identification numbers
    'TIN #':re.search('Tax ID :(.*)Type of Tax ID',content).group(1).strip(), #Page 4 Arrangement Tax ID
    'Practice Physical Address':re.search('CAQH Practice Location Number :(.*)\n\n(.*)\nStreet 1 :(.*)\n\nStreet 2 :(.*)Country :',content).group(3).strip(), #Page 3 Practice locations
    'Practice City':re.search('City :(.*)State :',content).group(1).strip(), #Page 3 Practice locations
    'Practice State':re.search('State :(.*)\n',content).group(1).strip(), #Page 3 Practice locations
    'Practice Zip':("-").join(re.findall('\d+',re.search('Zip Code :(.*)Email',content).group(1).strip())), #Page 3 Practice locations
    'Practice Phone #':("-").join(re.findall('\d+',re.search('Office Phone Number : (.*)Phone Extention :',content).group(1).strip())), #Page 3 Practice locations
    'Currently Practicing at this address?':re.search('Do you practice at this location\?:(.*)\n',content).group(1).strip(), #Page 3 Practice locations
    'Name of University':re.search('School :(.*)Street',content).group(1).strip(), #Page 2 - Education
    'Graduation Date':re.search('Start Date :(.*)End Date :(.*)\n',content).group(2).strip(), #Page 2 - Education
    'Degree Awarded':re.search('Degree :(.*)\n',content).group(1).strip(), #Page 2 - Education
}
with open('data.json', 'w') as outfile:
    json.dump(dict, outfile)
print(json.dumps(dict))
