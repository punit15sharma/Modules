#!/usr/bin/env /Users/zschillaci/Software/miniconda3/envs/pyenv/bin/python
from methods import *

recption_dir = INPUT_DIR + 'Oct2018/reception/'
recption_files = [
    'ABC130_M4_H2_HCC2_RC_0_0.txt',
    'ABC130_M4_H5_HCC5_RC_0_0.txt',
    'ABC130_M5_H3_HCC3_RC_0_0.txt',
    'ABC130_M5_H7_HCC6_RC_0_0.txt',
    'ABC130_M6_H0_HCC6_RC_0_0.txt',
    'ABC130_M6_H6_HCC12_RC_0_0.txt',
    'ABC130_M6_Hyb1_RC_0_0.txt',
    'ABC130_M6_Hyb4_RC_0_0.txt',
    'ABC130_M7_H1_HCC7_RC_0_0.txt',
    'ABC130_M7_H5_HCC11_RC_0_0.txt',
    'ABC130_M7_Hyb2_RC_0_0.txt',
    'ABC130_M7_Hyb4_RC_0_0.txt',
    # 'ABC130_M9_Hyb0_RC_0_0.txt',
    # 'ABC130_M9_Hyb6_RC_0_0.txt',
    'ABC130_M10_H1_HCC13_RC_0_0.txt',
    'ABC130_M10_H7_HCC6_RC_0_0.txt',
    'ABC130_M10_Hyb0_RC_0_0.txt',
    'ABC130_M10_Hyb7_RC_0_0.txt',
    'ABC130_M11_H3_HCC15_RC_0_0.txt',
    'ABC130_M11_H4_HCC14_RC_0_0.txt',
    'ABC130_M11_Hyb1_RC_0_0.txt',
    'ABC130_M11_Hyb7_RC_0_0.txt',
    'ABC130_M12_Hyb2_RC_0_0.txt',
    'ABC130_M12_Hyb6_RC_0_0.txt'
]

bnl_reception_dir = INPUT_DIR + 'Apr2019/'
bnl_reception_files = [
    'ABC130_BNL_20_1_RC_2799_56.txt',
    'ABC130_BNL_20_2_RC_2799_56.txt',
    'ABC130_BNL_21_1_RC_2858_47.txt',
    'ABC130_BNL_21_2_RC_2858_47.txt',
    'ABC130_BNL_22_1_RC_2815_47.txt',
    'ABC130_BNL_22_2_RC_2815_47.txt',
    'ABC130_BNL_23_1_RC_2856_47.txt',
    'ABC130_BNL_23_2_RC_2856_47.txt',
    'ABC130_BNL_24_1_RC_2857_47.txt',
    'ABC130_BNL_24_2_RC_2857_47.txt',
    'ABC130_BNL_25_1_RC_2866_54.txt',
    'ABC130_BNL_25_2_RC_2866_54.txt',
    'ABC130_BNL_26_1_RC_2868_47.txt',
    'ABC130_BNL_26_2_RC_2868_47.txt'
]

setPlotStyle()

recption_files_LBL = getFilesBySite(recption_files, site='LBL')
recption_files_SCIPP = getFilesBySite(recption_files, site='SCIPP')
recption_files_BNL = getFilesBySite(bnl_reception_files, site='BNL')

Reception_LBL = MultipleTestResults(recption_dir, recption_files_LBL, "Reception (LBL)")
Reception_SCIPP = MultipleTestResults(recption_dir, recption_files_SCIPP, "Reception (SCIPP)")
Reception_BNL = MultipleTestResults(bnl_reception_dir, recption_files_BNL, "Reception (BNL)")

plotMultiple([Reception_LBL, Reception_SCIPP, Reception_BNL], extension='Reception')

Individual_BNL = []
for bnl_module in BNL_MODULES:
    theName = bnl_module[0][:-2]
    
    theResult = MultipleTestResults(bnl_reception_dir, recption_files_BNL, theName, modules=bnl_module)
    Individual_BNL.append(theResult)

    plotMultipleVsChannel([theResult], extension=theName)

plotMultiple(Individual_BNL, extension='BNL', annotate=False)

