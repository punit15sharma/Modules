#!/usr/bin/env /Users/zschillaci/Software/miniconda3/envs/pyenv/bin/python
from methods import *

#Error Codes
# OrderedDict([(0, 'OK'), (4, 'inefficient'), (100, 'low gain'), (500, 'low gain'), (800, 'high offset'), (1000, 'unbonded'),
# (1100, 'low gain'), (1101, 'dead'), (1104, 'low gain'), (1500, 'lowgain'), (1501, 'dead'), (1504, 'low gain'), (4000, 'high noise'), 
# (4004, 'high noise'), (4100, 'low gain'), (4104, 'low gain'), (4500, 'low gain'), (4804, 'high offset'), (8000, 'partbonded')])
theBadCodes = ['low gain', 'lowgain', 'high noise', 'high offset',
               'partbonded', 'unbonded', 'inefficient', 'dead']

setPlotStyle()

Reception = ABC130_Site_Results(recption_dir, recption_files, "Reception")
Production = ABC130_Site_Results(production_dir, production_files, "Production")
plotMultiple([Reception, Production], extension='ALL')

print('ALL')
print('Reception:', str(len(recption_files)))
print('Production:', str(len(production_files)))

# print('RECEPTION')
recption_files_LBL = []
recption_files_SCIPP = []
for f in recption_files:
    for lbl, scipp in zip(LBL_modules, SCIPP_modules):
        if (lbl in f):
            # print('lbl', lbl, f)
            recption_files_LBL.append(f)
            break
        if (scipp in f):
            # print('scipp', scipp, f)
            recption_files_SCIPP.append(f)
            break

# print('PRODUCTION')
production_files_LBL = []
production_files_SCIPP = []
for f in production_files:
    for lbl, scipp in zip(LBL_modules, SCIPP_modules):
        if (lbl in f):
            # print('lbl', lbl, f)
            production_files_LBL.append(f)
            break
        if (scipp in f):
            # print('scipp', scipp, f)
            production_files_SCIPP.append(f)
            break

print('LBL')
print('Reception:', str(len(recption_files_LBL)))
print('Production:', str(len(production_files_LBL)))

print('SCIPP')
print('Reception:', str(len(recption_files_SCIPP)))
print('Production:', str(len(production_files_SCIPP)))

Reception_LBL = ABC130_Site_Results(recption_dir, recption_files_LBL, "Reception (LBL)")
Production_LBL = ABC130_Site_Results(production_dir, production_files_LBL, "Production (LBL)")
plotMultiple([Reception_LBL, Production_LBL], extension='LBL')

Reception_SCIPP = ABC130_Site_Results(recption_dir, recption_files_SCIPP, "Reception (SCIPP)")
Production_SCIPP = ABC130_Site_Results(production_dir, production_files_SCIPP, "Production (SCIPP)")
plotMultiple([Reception_SCIPP, Production_SCIPP], extension='SCIPP')
