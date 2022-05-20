
import os
import zipfile
import xml.etree.ElementTree as ET
import numpy as np
from astropy.io import ascii

program_type = 'GO-1' # ERS, GTO, GO-1
programs = [1837]


rt = '{http://www.stsci.edu/JWST/APT}'


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
        print(int(Target.find(f'{rt}Number').text), Target.find(f'{rt}EquatorialCoordinates').attrib['Value'])
        # print(Target.find(f'{rt}EquatorialCoordinates').attrib['Value'])


    print('-'*20)
    print('observations')
    print('-'*20)
    for observation in root.iter('{http://www.stsci.edu/JWST/APT}Observation'):

        o = {}
        for e in ['Number','TargetID','ScienceDuration','CoordinatedParallel','Instrument']:
            o[e] = observation.find(f'{{http://www.stsci.edu/JWST/APT}}{e}').text

        print('-'*10)
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

                # for e in ['Filter','Exposures','Groups','Integrations','Dither']:

                # print(c.tag)

        else:

            print('No NIRCam observations found')




        #
        # # --- now look at the properties of the prime observations
        # Template = observation.find('{http://www.stsci.edu/JWST/APT}Template')
        #
        # if o['Instrument'] == 'MIRI':
        #
        #     MiriImaging = Template.find('{http://www.stsci.edu/JWST/APT/Template/MiriImaging}MiriImaging')
        #
        #     for FilterConfig in MiriImaging.find('{http://www.stsci.edu/JWST/APT/Template/MiriImaging}Filters'):
        #         print('-----')
        #         for e in ['Filter','Exposures','Groups','Integrations','Dither']:
        #             print(e, FilterConfig.find(f'{{http://www.stsci.edu/JWST/APT/Template/MiriImaging}}{e}').text)
        #
        # if o['Instrument'] == 'NIRCAM':
        #
        #     pass
        #
        # # --- now look at the properties of the parallel observations
        #
        # if o['CoordinatedParallel'] == 'true':
        #
        #     CTemplate = observation.find('{http://www.stsci.edu/JWST/APT}FirstCoordinatedTemplate')
        #
        #     for c in CTemplate:
        #
        #
        #         print(c.tag)
