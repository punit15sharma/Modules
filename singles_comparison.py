#!/usr/bin/env /Users/zschillaci/Software/miniconda3/envs/pyenv/bin/python
from methods import *

setPlotStyle()

in_dir = INPUT_DIR + 'Feb2019/'
files = [ 
'ABC130_M6_Hyb1_RC_387_4.txt',
'ABC130_M6_Hyb1_RC_387_7.txt',
'ABC130_M6_Hyb4_RC_387_4.txt',
'ABC130_M6_Hyb4_RC_387_7.txt',
'ABC130_M7_H1_HCC7_RC_389_10.txt',
'ABC130_M7_H1_HCC7_RC_389_13.txt',
'ABC130_M7_H5_HCC11_RC_389_10.txt',
'ABC130_M7_H5_HCC11_RC_389_13.txt',
'ABC130_M7_Hyb2_RC_384_4.txt',
'ABC130_M7_Hyb2_RC_384_7.txt',
'ABC130_M7_Hyb4_RC_384_4.txt',
'ABC130_M7_Hyb4_RC_384_7.txt',
'ABC130_M9_Hyb0_RC_385_3.txt',
'ABC130_M9_Hyb0_RC_385_6.txt',
'ABC130_M9_Hyb6_RC_385_3.txt',
'ABC130_M9_Hyb6_RC_385_6.txt',
'ABC130_M10_H1_HCC13_RC_388_3.txt',
'ABC130_M10_H1_HCC13_RC_388_6.txt',
'ABC130_M10_H7_HCC6_RC_388_3.txt',
'ABC130_M10_H7_HCC6_RC_388_6.txt',
'ABC130_M11_Hyb1_RC_386_3.txt',
'ABC130_M11_Hyb1_RC_386_6.txt',
'ABC130_M11_Hyb7_RC_386_3.txt',
'ABC130_M11_Hyb7_RC_386_6.txt'
]

stave_files = [
    'ABC130_M6_Hyb1_RC_369_3.txt',
    'ABC130_M6_Hyb4_RC_369_3.txt',
    'ABC130_M7_H1_HCC7_RC_369_3.txt',
    'ABC130_M7_H5_HCC11_RC_369_3.txt',
    'ABC130_M7_Hyb2_RC_369_3.txt',
    'ABC130_M7_Hyb4_RC_369_3.txt',
    'ABC130_M9_Hyb0_RC_369_3.txt',
    'ABC130_M9_Hyb6_RC_369_3.txt',
    'ABC130_M10_H1_HCC13_RC_369_3.txt',
    'ABC130_M10_H7_HCC6_RC_369_3.txt',
    'ABC130_M11_Hyb1_RC_369_3.txt',
    'ABC130_M11_Hyb7_RC_369_3.txt'
]

n = 0
for i in range(len(files) - 3):
    if (i % 4 == 0):
        module = files[i][:files[i].index('RC') - 1]
        print('###--- ' + module + ' ---###')

        nonsingle_files = [files[i], files[i + 2]]
        single_files = [files[i + 1], files[i + 3]]

        fullstave_files = [stave_files[n], stave_files[n + 1]]
        n += 2

        nonsingle = MultipleTestResults(in_dir + 'corrected/', nonsingle_files, 'Non-Single')
        single = MultipleTestResults(in_dir + 'corrected/', single_files, 'Single')
        stave = MultipleTestResults(in_dir + 'stave/', fullstave_files, 'Full Stave') 

        plotMultiple([nonsingle, single, stave], extension='SinglesComparison-' + module)
        print('')
