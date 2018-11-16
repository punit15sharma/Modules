#!/usr/bin/env /Users/zschillaci/Software/miniconda3/envs/pyenv/bin/python
from methods import *

#Error Codes
# OrderedDict([(0, 'OK'), (4, 'inefficient'), (100, 'low gain'), (500, 'low gain'), (800, 'high offset'), (1000, 'unbonded'),
# (1100, 'low gain'), (1101, 'dead'), (1104, 'low gain'), (1500, 'lowgain'), (1501, 'dead'), (1504, 'low gain'), (4000, 'high noise'), 
# (4004, 'high noise'), (4100, 'low gain'), (4104, 'low gain'), (4500, 'low gain'), (4804, 'high offset'), (8000, 'partbonded')])
theBadCodes = ['low gain', 'lowgain', 'high noise', 'high offset',
               'partbonded', 'unbonded', 'inefficient', 'dead']

setPlotStyle()

print('--- All --- ')
print('Reception:', str(len(recption_files)))
print('Production:', str(len(production_files)))
print('Stave:', str(len(stave_files)))

recption_files_LBL, recption_files_SCIPP = GetFilesBySite(recption_files)

production_files_LBL, production_files_SCIPP = GetFilesBySite(production_files)

stave_files_LBL, stave_files_SCIPP = GetFilesBySite(stave_files)

print('--- LBL --- ')
print('Reception:', str(len(recption_files_LBL)))
print('Production:', str(len(production_files_LBL)))
print('Stave:', str(len(stave_files_LBL)))

print('--- SCIPP --- ')
print('Reception:', str(len(recption_files_SCIPP)))
print('Production:', str(len(production_files_SCIPP)))
print('Stave:', str(len(stave_files_SCIPP)))

Reception = ABC130_Site_Results(recption_dir, recption_files, "Reception (All)")
Production = ABC130_Site_Results(production_dir, production_files, "Production (All)")
Stave = ABC130_Site_Results(stave_dir, stave_files, "Stave (All)")

plotMultiple([Reception, Production, Stave], extension='All')

Reception_LBL = ABC130_Site_Results(recption_dir, recption_files_LBL, "Reception (LBL)")
Production_LBL = ABC130_Site_Results(production_dir, production_files_LBL, "Production (LBL)")
Stave_LBL = ABC130_Site_Results(stave_dir, stave_files_LBL, "Stave (LBL)")

plotMultiple([Reception_LBL, Production_LBL, Stave_LBL], extension='LBL')
plotMultiple([Reception_LBL, Production_LBL, Stave_LBL], extension='LBL-Ch1792-1920', channels=[1792, 1792 + 128])

Reception_SCIPP = ABC130_Site_Results(recption_dir, recption_files_SCIPP, "Reception (SCIPP)")
Production_SCIPP = ABC130_Site_Results(production_dir, production_files_SCIPP, "Production (SCIPP)")
Stave_SCIPP = ABC130_Site_Results(stave_dir, stave_files_SCIPP, "Stave (SCIPP)")

plotMultiple([Reception_SCIPP, Production_SCIPP, Stave_SCIPP], extension='SCIPP')
plotMultiple([Reception_SCIPP, Production_SCIPP, Stave_SCIPP], extension='SCIPP-Ch1792-1920', channels=[1792, 1792 + 128])

#LBL11
LBL11 = ['ABC130_M11_H3_HCC15', 'ABC130_M11_H4_HCC14']

Reception_LBL11 = ABC130_Site_Results(recption_dir, recption_files_LBL, "Reception (LBL11)", modules=LBL11)
Production_LBL11 = ABC130_Site_Results(production_dir, production_files_LBL, "Production (LBL11)", modules=LBL11)
Stave_LBL11 = ABC130_Site_Results(stave_dir, stave_files_LBL, "Stave (LBL11)", modules=LBL11)

plotMultiple([Reception_LBL11, Production_LBL11, Stave_LBL11], extension='LBL11')
plotMultiple([Reception_LBL11, Production_LBL11, Stave_LBL11], extension='LBL11-Ch1792-1920', channels=[1792, 1792 + 128])

plotMultipleVsChannel([Reception_LBL11, Production_LBL11, Stave_LBL11], extension='LBL11', channels=[1792, 1792 + 128])