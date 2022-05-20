

import pycurl
import os
import zipfile

url = "https://www.stsci.edu/"
path = "jwst/phase2-public/"

# programs = [p.strip() for p in open('apts/GTO_list.csv','r').readlines()]

program_type = 'GTO-1' # this could be ERS, GO-1, GTO-1 etc.
programs = ['2738']

for program in programs:

    # --- download
    filename = program+'.aptx'
    fp = open(f'apts/{program_type}/{filename}', "wb")
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, url+path+filename)
    curl.setopt(pycurl.WRITEDATA, fp)
    curl.perform()
    curl.close()
    fp.close()

    # --- convert to XML
    zip = zipfile.ZipFile(f'apts/{program_type}/{program}.aptx', 'r')
    xmlfile=f'{program}.xml'  #makes a string of the xml file's name.
    r = zip.open(xmlfile).read()
    with open(f'apts/{program_type}/{xmlfile}', 'wb') as xfile:
        xfile.write(r)
