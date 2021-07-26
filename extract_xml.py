
import os
import zipfile

# this code extracts an .xml file from the .aptx files.

program_type = 'GO-1' # ERS, GTO, GO-1
programs = [1837]
# programs = set([file.split('.')[0] for file in os.listdir(f'apts/{program_type}/')]) # get a list of all programmes

for program in programs:
    zip = zipfile.ZipFile(f'apts/{program_type}/{program}.aptx', 'r')
    xmlfile=f'{program}.xml'  #makes a string of the xml file's name.
    r = zip.open(xmlfile).read()
    with open(f'apts/{program_type}/{xmlfile}', 'wb') as xfile:
        xfile.write(r)
