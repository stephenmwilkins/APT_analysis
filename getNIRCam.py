
import os
import zipfile
import xml.etree.ElementTree as ET
import numpy as np
from astropy.io import ascii

rt = '{http://www.stsci.edu/JWST/APT}'

# program_type = 'GO-1' # ERS, GTO, GO-1
# programs = [1837]

program_type = 'GTO-1'
programs = [2738]


for program in programs:

    print('-'*50)
    print(program)

    zipf = zipfile.ZipFile(f'apts/{program_type}/{program}.aptx', 'r')

    r = zipf.open(f'{program}.xml').read()

    root = ET.fromstring(r)

    # --- loop over targets

    print('-'*20)
    print('TARGETS')
    print('-'*20)
    for Target in root.iter(f'{rt}Target'):

        # for child in Target:
        #     tag = child.tag.split('}')[-1]
        #     print(tag, child.text)

        print(int(Target.find(f'{rt}Number').text), Target.find(f'{rt}TargetName').text, Target.find(f'{rt}EquatorialCoordinates').attrib['Value'])
        # print(Target.find(f'{rt}EquatorialCoordinates').attrib['Value'])


    print('-'*20)
    print('observations')
    print('-'*20)
    for observation in root.iter('{http://www.stsci.edu/JWST/APT}Observation'):

        print('-'*10)

        try:

            o = {}
            for e in ['Number','TargetID','ScienceDuration','CoordinatedParallel','Instrument']:
                o[e] = observation.find(f'{{http://www.stsci.edu/JWST/APT}}{e}').text


            print(f'Observation: {o["Number"]}')
            print('-'*10)

            for e in ['TargetID','ScienceDuration','CoordinatedParallel','Instrument']:
                print(e, o[e])

            NIRCam = observation.findall('.//{http://www.stsci.edu/JWST/APT/Template/NircamImaging}NircamImaging')

            if len(NIRCam)>0:

                NIRCam = NIRCam[0] #
                Filters = NIRCam.findall('.//{http://www.stsci.edu/JWST/APT/Template/NircamImaging}Filters')[0]
                for i, FilterConfig in enumerate(Filters):
                    print('----', i)
                    nircam_obs = {}
                    for c in FilterConfig:
                        tag = c.tag.split('}')[-1]
                        print(tag, c.text)

            else:
                print('No NIRCam observations found')


        except:
            print('failed for this observation')
            print('-'*10)
