

import pycurl

url = "https://www.stsci.edu/"
path = "jwst/phase2-public/"



programs = [p.strip() for p in open('apts/GTO_list.csv','r').readlines()]

print(programs)


for program in programs:

    print(program)
    filename = program+'.aptx'
    fp = open(f'apts/GTO/{filename}', "wb")
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, url+path+filename)
    curl.setopt(pycurl.WRITEDATA, fp)
    curl.perform()
    curl.close()
    fp.close()
