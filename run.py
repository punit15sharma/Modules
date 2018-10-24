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

plotMultiple([Reception,Production])

