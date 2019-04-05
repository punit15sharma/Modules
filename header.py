#!/usr/bin/env /Users/zschillaci/Software/miniconda3/envs/pyenv/bin/python
import os
import csv
import collections
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def getModulesFromHybrids(hybrids):
    modules = []
    for i in range(len(hybrids) - 1):
        if (i % 2 == 0):
            modules.append([hybrids[i], hybrids[i + 1]])
    return modules

LBL_HYBRIDS = [
'ABC130_M11_H3_HCC15',
'ABC130_M11_H4_HCC14',
'ABC130_M10_H1_HCC13',
'ABC130_M10_H7_HCC6',
'ABC130_M7_H1_HCC7',
'ABC130_M7_H5_HCC11',
'ABC130_M5_H3_HCC3',
'ABC130_M5_H7_HCC6',
'ABC130_M4_H2_HCC2',
'ABC130_M4_H5_HCC5',
'ABC130_M6_H0_HCC6',
'ABC130_M6_H6_HCC12'
]
LBL_MODULES = getModulesFromHybrids(LBL_HYBRIDS)

SCIPP_HYBRIDS = [
'ABC130_M12_Hyb2',
'ABC130_M12_Hyb6',
'ABC130_M11_Hyb1',
'ABC130_M11_Hyb7',
'ABC130_M10_Hyb0',
'ABC130_M10_Hyb7',
'ABC130_M9_Hyb0',
'ABC130_M9_Hyb6',
'ABC130_M7_Hyb2',
'ABC130_M7_Hyb4',
'ABC130_M6_Hyb1',
'ABC130_M6_Hyb4'
]
SCIPP_MODULES = getModulesFromHybrids(SCIPP_HYBRIDS)

BNL_HYBRIDS = [
'ABC130_BNL_20_1',
'ABC130_BNL_20_2',
'ABC130_BNL_21_1',
'ABC130_BNL_21_2',
'ABC130_BNL_22_1',
'ABC130_BNL_22_2',
'ABC130_BNL_23_1',
'ABC130_BNL_23_2',
'ABC130_BNL_24_1',
'ABC130_BNL_24_2',
'ABC130_BNL_25_1',
'ABC130_BNL_25_2',
'ABC130_BNL_26_1',
'ABC130_BNL_26_2',
# 'ABC130_BNL_27_1',
# 'ABC130_BNL_27_2'
]
BNL_MODULES = getModulesFromHybrids(BNL_HYBRIDS)

SITES = {'LBL'      : LBL_HYBRIDS,
         'SCIPP'    : SCIPP_HYBRIDS,
         'BNL'      : BNL_HYBRIDS}

INPUT_DIR = '/Users/zschillaci/BNL/Working/InnerTracker/Modules/input/'
RESULTS_DIR = '/Users/zschillaci/BNL/Working/InnerTracker/Modules/results/'

#Error Codes
# OrderedDict([(0, 'OK'), (4, 'inefficient'), (100, 'low gain'), (500, 'low gain'), (800, 'high offset'), (1000, 'unbonded'),
# (1100, 'low gain'), (1101, 'dead'), (1104, 'low gain'), (1500, 'lowgain'), (1501, 'dead'), (1504, 'low gain'), (4000, 'high noise'),
# (4004, 'high noise'), (4100, 'low gain'), (4104, 'low gain'), (4500, 'low gain'), (4804, 'high offset'), (8000, 'partbonded')])
ALL_BAD_CODES = ['low gain', 'lowgain', 'high noise', 'high offset', 'partbonded', 'unbonded', 'inefficient', 'dead']
FAILURE_CODES = ['dead']
