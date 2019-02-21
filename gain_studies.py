#!/usr/bin/env /Users/zschillaci/Software/miniconda3/envs/pyenv/bin/python
from methods import *

setPlotStyle()

in_dir = INPUT_DIR + 'Nov2018/'

scipp_files = [
    # 'modules_SCIPP_SCIPP-EL-14_wPB_results_ABC130_M14_Hyb3_RC_11_27.txt',
    # 'modules_SCIPP_SCIPP-EL-14_wPB_results_ABC130_M14_Hyb3_RC_11_3.txt',
    # 'modules_SCIPP_SCIPP-EL-14_wPB_results_ABC130_M14_Hyb3_RC_11_30.txt',
    'modules_SCIPP_SCIPP-EL-14_wPB_results_ABC130_M14_Hyb3_RC_11_40.txt',
    'modules_SCIPP_SCIPP-EL-14_wPB_results_ABC130_M14_Hyb4_RC_11_27.txt',
    # 'modules_SCIPP_SCIPP-EL-14_wPB_results_ABC130_M14_Hyb4_RC_11_3.txt',
    # 'modules_SCIPP_SCIPP-EL-14_wPB_results_ABC130_M14_Hyb4_RC_11_30.txt',
    # 'modules_SCIPP_SCIPP-EL-14_wPB_results_ABC130_M14_Hyb4_RC_11_40.txt'
            ]

SCIPP = ABC130_Site_Results(in_dir + 'SCIPP/', scipp_files, 'SCIPP')

files = ['ABC130_M14_Hyb3_RC_2529_2.txt', 'ABC130_M14_Hyb4_RC_2529_2.txt']
BNL_scipp_config_15degrees = ABC130_Site_Results(in_dir + 'BNL/scipp_config_15degrees/', files, 'scipp_config_15degrees')

files = ['ABC130_M14_Hyb3_RC_2524_1.txt', 'ABC130_M14_Hyb4_RC_2524_1.txt']
BNL_scipp_config_17degrees = ABC130_Site_Results(in_dir + 'BNL/scipp_config_17degrees/', files, 'scipp_config_17degrees')

files = ['ABC130_M14_Hyb3_RC_2529_7.txt', 'ABC130_M14_Hyb4_RC_2529_7.txt']
BNL_tuned_15degrees = ABC130_Site_Results(in_dir + 'BNL/tuned_15degrees/', files, 'tuned_15degrees')

files = ['ABC130_M14_Hyb3_RC_2524_6.txt', 'ABC130_M14_Hyb4_RC_2524_6.txt']
BNL_tuned_17degrees = ABC130_Site_Results(in_dir + 'BNL/tuned_17degrees/', files, 'tuned_17degrees')

toPlot = [SCIPP, BNL_scipp_config_15degrees]
plotMultiple(toPlot, extension='GainComparisons-scippConfig')

toPlot = [SCIPP, BNL_tuned_15degrees]
plotMultiple(toPlot, extension='GainComparisons-tuned')
