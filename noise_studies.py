#!/usr/bin/env /Users/zschillaci/Software/miniconda3/envs/pyenv/bin/python
from methods import *

setPlotStyle()

in_dir = INPUT_DIR + 'Feb2019/'

individual_files = [
'ABC130_M4_H2_HCC2_RC_363_3.txt',
'ABC130_M4_H5_HCC5_RC_363_3.txt',
'ABC130_M5_H3_HCC3_RC_357_3.txt',
'ABC130_M5_H7_HCC6_RC_357_3.txt',
'ABC130_M6_H0_HCC6_RC_368_4.txt',
'ABC130_M6_H6_HCC12_RC_368_4.txt',
'ABC130_M6_Hyb1_RC_356_3.txt',
'ABC130_M6_Hyb4_RC_356_3.txt',
'ABC130_M7_H1_HCC7_RC_366_6.txt',
'ABC130_M7_H5_HCC11_RC_366_6.txt',
'ABC130_M7_Hyb2_RC_346_7.txt',
'ABC130_M7_Hyb4_RC_346_7.txt',
'ABC130_M9_Hyb0_RC_349_5.txt',
'ABC130_M9_Hyb6_RC_349_5.txt',
'ABC130_M10_H1_HCC13_RC_358_3.txt',
'ABC130_M10_H7_HCC6_RC_358_3.txt',
'ABC130_M10_Hyb0_RC_351_6.txt',
'ABC130_M10_Hyb7_RC_351_6.txt',
'ABC130_M11_H3_HCC15_RC_365_3.txt',
'ABC130_M11_H4_HCC14_RC_365_3.txt',
'ABC130_M11_Hyb1_RC_352_3.txt',
'ABC130_M11_Hyb7_RC_352_3.txt',
'ABC130_M12_Hyb2_RC_355_3.txt',
'ABC130_M12_Hyb6_RC_355_3.txt'
]

stave_files = [
'ABC130_M4_H2_HCC2_RC_369_3.txt',
'ABC130_M4_H5_HCC5_RC_369_3.txt',
'ABC130_M5_H3_HCC3_RC_369_3.txt',
'ABC130_M5_H7_HCC6_RC_369_3.txt',
'ABC130_M6_H0_HCC6_RC_369_3.txt',
'ABC130_M6_H6_HCC12_RC_369_3.txt',
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
'ABC130_M10_Hyb0_RC_369_3.txt',
'ABC130_M10_Hyb7_RC_369_3.txt',
'ABC130_M11_H3_HCC15_RC_369_3.txt',
'ABC130_M11_H4_HCC14_RC_369_3.txt',
'ABC130_M11_Hyb1_RC_369_3.txt',
'ABC130_M11_Hyb7_RC_369_3.txt',
'ABC130_M12_Hyb2_RC_369_3.txt',
'ABC130_M12_Hyb6_RC_369_3.txt'
]

psupply_files = [
'ABC130_M4_H2_HCC2_RC_370_3.txt',
'ABC130_M4_H5_HCC5_RC_370_3.txt',
'ABC130_M5_H3_HCC3_RC_370_3.txt',
'ABC130_M5_H7_HCC6_RC_370_3.txt',
'ABC130_M6_H0_HCC6_RC_370_3.txt',
'ABC130_M6_H6_HCC12_RC_370_3.txt',
'ABC130_M6_Hyb1_RC_370_3.txt',
'ABC130_M6_Hyb4_RC_370_3.txt',
'ABC130_M7_H1_HCC7_RC_370_3.txt',
'ABC130_M7_H5_HCC11_RC_370_3.txt',
'ABC130_M7_Hyb2_RC_370_3.txt',
'ABC130_M7_Hyb4_RC_370_3.txt',
'ABC130_M9_Hyb0_RC_370_3.txt',
'ABC130_M9_Hyb6_RC_370_3.txt',
'ABC130_M10_H1_HCC13_RC_370_3.txt',
'ABC130_M10_H7_HCC6_RC_370_3.txt',
'ABC130_M10_Hyb0_RC_370_3.txt',
'ABC130_M10_Hyb7_RC_370_3.txt',
'ABC130_M11_H3_HCC15_RC_370_3.txt',
'ABC130_M11_H4_HCC14_RC_370_3.txt',
'ABC130_M11_Hyb1_RC_370_3.txt',
'ABC130_M11_Hyb7_RC_370_3.txt',
'ABC130_M12_Hyb2_RC_370_3.txt',
'ABC130_M12_Hyb6_RC_370_3.txt'
]

for i in range(len(individual_files) - 1):
    if (i % 2 == 0):
        infiles = [individual_files[i], individual_files[i + 1]]
        individual = ABC130_Site_Results(in_dir + 'individual/', infiles, 'Individual')

        infiles = [stave_files[i], stave_files[i + 1]]
        stave = ABC130_Site_Results(in_dir + 'stave/', infiles, 'Stave')

        infiles = [psupply_files[i], psupply_files[i + 1]]
        psupply = ABC130_Site_Results(in_dir + 'psupply/', infiles, '10V')

        module = individual_files[i][:-13]

        plotMultiple([individual, stave], extension='Ind-vs-Stave-' + module)
        plotMultiple([psupply, stave], extension='Psupply-vs-Stave-' + module)