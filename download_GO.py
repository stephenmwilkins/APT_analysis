

import pycurl

url = "https://www.stsci.edu/"
path = "jwst/phase2-public/"


programs = [1433]

print(programs)


for program in programs:

    print(program)
    filename = str(program)+'.aptx'
    fp = open(f'apts/GO-1/{filename}', "wb")
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, url+path+filename)
    curl.setopt(pycurl.WRITEDATA, fp)
    curl.perform()
    curl.close()
    fp.close()
