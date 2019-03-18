#!/usr/bin/env /Users/zschillaci/Software/miniconda3/envs/pyenv/bin/python
from methods import *

#Error Codes
# OrderedDict([(0, 'OK'), (4, 'inefficient'), (100, 'low gain'), (500, 'low gain'), (800, 'high offset'), (1000, 'unbonded'),
# (1100, 'low gain'), (1101, 'dead'), (1104, 'low gain'), (1500, 'lowgain'), (1501, 'dead'), (1504, 'low gain'), (4000, 'high noise'), 
# (4004, 'high noise'), (4100, 'low gain'), (4104, 'low gain'), (4500, 'low gain'), (4804, 'high offset'), (8000, 'partbonded')])
theBadCodes = ['low gain', 'lowgain', 'high noise', 'high offset',
               'partbonded', 'unbonded', 'inefficient', 'dead']

production_dir = INPUT_DIR + 'Oct2018/production/'
production_files = [
    'ABC130_M4_H2_HCC2_RC_2_40.txt',
    'ABC130_M4_H5_HCC5_RC_2_40.txt',
    'ABC130_M5_H3_HCC3_RC_2_40.txt',
    'ABC130_M5_H7_HCC6_RC_2_40.txt',
    'ABC130_M6_H0_HCC6_RC_2_40.txt',
    'ABC130_M6_H6_HCC12_RC_2_40.txt',
    'ABC130_M6_Hyb1_RC_2_40.txt',
    'ABC130_M6_Hyb4_RC_2_40.txt',
    'ABC130_M7_H1_HCC7_RC_2_40.txt',
    'ABC130_M7_H5_HCC11_RC_2_40.txt',
    'ABC130_M7_Hyb2_RC_2_40.txt',
    'ABC130_M7_Hyb4_RC_2_40.txt',
    # 'ABC130_M9_Hyb0_RC_2_40.txt',
    # 'ABC130_M9_Hyb6_RC_2_40.txt',
    'ABC130_M10_H1_HCC13_RC_2_40.txt',
    'ABC130_M10_H7_HCC6_RC_2_40.txt',
    'ABC130_M10_Hyb0_RC_2_40.txt',
    'ABC130_M10_Hyb7_RC_2_40.txt',
    'ABC130_M11_H3_HCC15_RC_2_40.txt',
    'ABC130_M11_H4_HCC14_RC_2_40.txt',
    'ABC130_M11_Hyb1_RC_2_40.txt',
    'ABC130_M11_Hyb7_RC_2_40.txt',
    'ABC130_M12_Hyb2_RC_2_40.txt',
    'ABC130_M12_Hyb6_RC_2_40.txt']

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
    'ABC130_M12_Hyb6_RC_0_0.txt']

stave_dir = INPUT_DIR + 'Oct2018/stave/'
stave_files = [
    'ABC130_M4_H2_HCC2_RC_236_5.txt',
    'ABC130_M4_H5_HCC5_RC_236_5.txt',
    'ABC130_M5_H3_HCC3_RC_236_5.txt',
    'ABC130_M5_H7_HCC6_RC_236_5.txt',
    'ABC130_M6_H0_HCC6_RC_236_5.txt',
    'ABC130_M6_H6_HCC12_RC_236_5.txt',
    'ABC130_M6_Hyb1_RC_236_5.txt',
    'ABC130_M6_Hyb4_RC_236_5.txt',
    'ABC130_M7_H1_HCC7_RC_236_5.txt',
    'ABC130_M7_H5_HCC11_RC_236_5.txt',
    'ABC130_M7_Hyb2_RC_236_5.txt',
    'ABC130_M7_Hyb4_RC_236_5.txt',
    # 'ABC130_M9_Hyb0_RC_236_5.txt',
    # 'ABC130_M9_Hyb6_RC_236_5.txt',
    'ABC130_M10_H1_HCC13_RC_236_5.txt',
    'ABC130_M10_H7_HCC6_RC_236_5.txt',
    'ABC130_M10_Hyb0_RC_236_5.txt',
    'ABC130_M10_Hyb7_RC_236_5.txt',
    'ABC130_M11_H3_HCC15_RC_236_5.txt',
    'ABC130_M11_H4_HCC14_RC_236_5.txt',
    'ABC130_M11_Hyb1_RC_236_5.txt',
    'ABC130_M11_Hyb7_RC_236_5.txt',
    'ABC130_M12_Hyb2_RC_236_5.txt',
    'ABC130_M12_Hyb6_RC_236_5.txt']

setPlotStyle()

print('--- All --- ')
print('Production:', str(len(production_files)))
print('Reception:', str(len(recption_files)))
print('Stave:', str(len(stave_files)))

production_files_LBL = getFilesBySite(production_files, site='LBL')
production_files_SCIPP = getFilesBySite(production_files, site='SCIPP')

recption_files_LBL = getFilesBySite(recption_files, site='LBL')
recption_files_SCIPP = getFilesBySite(recption_files, site='SCIPP')

stave_files_LBL = getFilesBySite(stave_files, site='LBL')
stave_files_SCIPP = getFilesBySite(stave_files, site='SCIPP')

print('--- LBL --- ')
print('Production:', str(len(production_files_LBL)))
print('Reception:', str(len(recption_files_LBL)))
print('Stave:', str(len(stave_files_LBL)))

print('--- SCIPP --- ')
print('Production:', str(len(production_files_SCIPP)))
print('Reception:', str(len(recption_files_SCIPP)))
print('Stave:', str(len(stave_files_SCIPP)))

Production = MultipleTestResults(production_dir, production_files, "Production (All)")
Reception = MultipleTestResults(recption_dir, recption_files, "Reception (All)")
Stave = MultipleTestResults(stave_dir, stave_files, "Stave (All)")

plotMultiple([Production, Reception, Stave], extension='All')
plotMultiple([Production, Reception, Stave], extension='All-Ch1792-1920', channels=[1792, 1792 + 128])

Production_LBL = MultipleTestResults(production_dir, production_files_LBL, "Production (LBL)")
Reception_LBL = MultipleTestResults(recption_dir, recption_files_LBL, "Reception (LBL)")
Stave_LBL = MultipleTestResults(stave_dir, stave_files_LBL, "Stave (LBL)")

plotMultiple([Production_LBL, Reception_LBL, Stave_LBL], extension='LBL')
plotMultiple([Production_LBL, Reception_LBL, Stave_LBL], extension='LBL-Ch1792-1920', channels=[1792, 1792 + 128])

Production_SCIPP = MultipleTestResults(production_dir, production_files_SCIPP, "Production (SCIPP)")
Reception_SCIPP = MultipleTestResults(recption_dir, recption_files_SCIPP, "Reception (SCIPP)")
Stave_SCIPP = MultipleTestResults(stave_dir, stave_files_SCIPP, "Stave (SCIPP)")

plotMultiple([Production_SCIPP, Reception_SCIPP, Stave_SCIPP], extension='SCIPP')
plotMultiple([Production_SCIPP, Reception_SCIPP, Stave_SCIPP], extension='SCIPP-Ch1792-1920', channels=[1792, 1792 + 128])

#LBL11
LBL11 = ['ABC130_M11_H3_HCC15', 'ABC130_M11_H4_HCC14']

Production_LBL11 = MultipleTestResults(production_dir, production_files_LBL, "Production (LBL11)", modules=LBL11)
Reception_LBL11 = MultipleTestResults(recption_dir, recption_files_LBL, "Reception (LBL11)", modules=LBL11)
Stave_LBL11 = MultipleTestResults(stave_dir, stave_files_LBL, "Stave (LBL11)", modules=LBL11)

plotMultiple([Production_LBL11, Reception_LBL11, Stave_LBL11], extension='LBL11')
plotMultiple([Production_LBL11, Reception_LBL11, Stave_LBL11], extension='LBL11-Ch1792-1920', channels=[1792, 1792 + 128])

plotMultipleVsChannel([Production_LBL11, Reception_LBL11, Stave_LBL11], extension='LBL11', channels=[1792, 1792 + 128])
