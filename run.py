#!/usr/bin/python
from methods import *

#Error Codes
# OrderedDict([(0, 'OK'), (4, 'inefficient'), (100, 'low gain'), (500, 'low gain'), (800, 'high offset'), (1000, 'unbonded'),
# (1100, 'low gain'), (1101, 'dead'), (1104, 'low gain'), (1500, 'lowgain'), (1501, 'dead'), (1504, 'low gain'), (4000, 'high noise'), 
# (4004, 'high noise'), (4100, 'low gain'), (4104, 'low gain'), (4500, 'low gain'), (4804, 'high offset'), (8000, 'partbonded')])
theBadCodes = ['low gain', 'lowgain', 'high noise', 'high offset',
               'partbonded', 'unbonded', 'inefficient', 'dead']

setPlotStyle()
# BNL23_ABC130 = ABC130_Single_Result(directory, 'ABC130_M1_BNL_RC_32828_23.txt', 'BNL_23')
# BNL10_ABC130 = ABC130_Single_Result(directory, 'ABC130_M1_BNL_RC_32832_10.txt', 'BNL_10')
# BNL5_ABC130 = ABC130_Single_Result(directory, 'ABC130_M1_BNL_RC_32832_5.txt', 'BNL_5')

# LBNL4_ABC130 = ABC130_Single_Result(directory, 'ABC130_M2_LBNL_RC_32913_4.txt', 'LBNL_4')
# LBNL8_ABC130 = ABC130_Single_Result(directory, 'ABC130_M1_LBNL_RC_32912_8.txt', 'LBNL_8')
# LBNL3_ABC130 = ABC130_Single_Result(directory, 'ABC130_M1_LBNL_RC_32909_3.txt', 'LBNL_3')

# SCIPP31_ABC130 = ABC130_Single_Result(directory, 'ABC130_SCIPP01_PXH3_RC_32878_31.txt', 'SCIPP_31')
# SCIPP34_ABC130 = ABC130_Single_Result(directory, 'ABC130_SCIPP01_PXH3_RC_32878_34.txt', 'SCIPP_34')
# SCIPP3_ABC130 = ABC130_Single_Result(directory, 'ABC130_SCIPP_M7_Hyb2_RC_32929_3.txt', 'SCIPP_3')

# BNL10_ABC130.plot(selections = ['low gain'])
# plotMultipleResults([BNL23_ABC130, BNL10_ABC130, BNL5_ABC130])
# plotMultipleResults([LBNL4_ABC130, LBNL8_ABC130, LBNL3_ABC130])
# plotMultipleResults([SCIPP31_ABC130, SCIPP34_ABC130, SCIPP3_ABC130])
# plotMultipleResults([BNL23_ABC130, LBNL4_ABC130, SCIPP31_ABC130])

BNL_ABC130 = ABC130_Site_Results(directory, BNL_Results, "BNL")
LBNL_ABC130 = ABC130_Site_Results(directory, LBNL_Results, "LBNL")
SCIPP_ABC130 = ABC130_Site_Results(directory, SCIPP_Results, "SCIPP")

# BNL_ABC130.plot()
# LBNL_ABC130.plot()
# SCIPP_ABC130.plot()
plotMultiple([BNL_ABC130, LBNL_ABC130, SCIPP_ABC130])
plotMultiple([BNL_ABC130,LBNL_ABC130,SCIPP_ABC130],selections=['OK'])
plotMultiple([BNL_ABC130,LBNL_ABC130,SCIPP_ABC130],unselections=['OK'])

