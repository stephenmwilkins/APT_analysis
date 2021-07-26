
import os
import zipfile
import xml.etree.ElementTree as ET
import numpy as np
from astropy.io import ascii

program_type = 'GO-1' # ERS, GTO, GO-1
programs = [1837]


rt = '{http://www.stsci.edu/JWST/APT}'


for program in programs:

    print('-'*20)
    print(program)

    zipf = zipfile.ZipFile(f'apts/{program_type}/{program}.aptx', 'r')

    r = zipf.open(f'{program}.xml').read()

    root = ET.fromstring(r)

    # --- loop over targets

    for Target in root.iter(f'{rt}Target'):
        print(int(Target.find(f'{rt}Number').text))
        print(Target.find(f'{rt}EquatorialCoordinates').attrib['Value'])
        # print(Target.find(f'{rt}EquatorialCoordinates').attrib['Value'])



    # for observation in root.iter('{http://www.stsci.edu/JWST/APT}Observation'):
    #
    #     try:
    #         TargetID = observation.find('{http://www.stsci.edu/JWST/APT}TargetID').text
    #         TargetNumber = int(TargetID.split(' ')[0])
    #         ScienceDuration = int(observation.find('{http://www.stsci.edu/JWST/APT}ScienceDuration').text)
    #         CoordinatedParallel = observation.find('{http://www.stsci.edu/JWST/APT}CoordinatedParallel').text
    #
    #         Instrument = observation.find('{http://www.stsci.edu/JWST/APT}Instrument').text
    #
    #         if wCP:
    #             TargetScienceDuration[TargetNumber].append(ScienceDuration)
    #             TargetInstrument[TargetNumber].append(Instrument)
    #
    #         if not wCP:
    #             if CoordinatedParallel == 'false':
    #                 TargetScienceDuration[TargetNumber].append(ScienceDuration)
    #                 TargetInstrument[TargetNumber].append(Instrument)
    #
    #     except:
    #         print('could not extract observation')
    #
    #
    #
    #
    # for TargetNumber, ScienceDurations in TargetScienceDuration.items():
    #
    #     Nobs = len(ScienceDurations)
    #
    #     print(TargetInstrument[TargetNumber])
    #
    #     if Nobs >0:
    #
    #         for inst in set(TargetInstrument[TargetNumber]):
    #
    #             s = np.array(TargetInstrument[TargetNumber])==inst
    #
    #             cat['Program'].append(Program)
    #             cat['ProgramType'].append(ProgramType)
    #             cat['EquatorialCoordinates'].append(EquatorialCoordinates[TargetNumber])
    #             ScienceDuration = np.sum(np.array(ScienceDurations)[s])
    #             cat['ScienceDuration'].append(ScienceDuration)
    #             cat['Instrument'].append(inst)
    #             cat['Nobs'].append(len(np.array(ScienceDurations)[s]))



# ascii.write(cat, f'tables/programs_{program_type}.cat', overwrite=True)
