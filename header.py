#!/usr/bin/python
import csv
import collections
import numpy as np
import matplotlib.pyplot as plt

def setPlotStyle():
    plt.style.use('ggplot')
    plt.rcParams['lines.linewidth'] = 2.15
    plt.rcParams['lines.markeredgewidth'] = 0.0
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.facecolor'] = 'whitesmoke'
    plt.rcParams['grid.color'] = 'black'
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['grid.linewidth'] = '0.25'
    plt.rcParams['grid.alpha'] = '0.25'
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['legend.fontsize'] = 10
    plt.rcParams['legend.frameon'] = False
    plt.rcParams['figure.titlesize'] = 'large'
    plt.rcParams['figure.titleweight'] = 'bold'
    plt.rcParams['axes.edgecolor'] = 'black'
    plt.rcParams['patch.edgecolor'] = 'none'
    plt.rcParams.update({'figure.max_open_warning': 0})

directory = '/Users/TheUniverse/BNL/Working/modules/BNL_Test_Data/DATA/results/'

BNL_Results = ['ABC130_M1_BNL_RC_32828_23.txt', 'ABC130_M1_BNL_RC_32836_4.txt', 'ABC130_M1_BNL_RC_32870_3.txt',
               'ABC130_M1_BNL_RC_32832_10.txt', 'ABC130_M1_BNL_RC_32866_7.txt', 'ABC130_M1_BNL_RC_32870_30.txt',
               'ABC130_M1_BNL_RC_32832_5.txt',  'ABC130_M1_BNL_RC_32869_7.txt', 'ABC130_M1_BNL_RC_32870_40.txt',
               'ABC130_M1_BNL_RC_32835_6.txt',  'ABC130_M1_BNL_RC_32870_27.txt',

               'ABC130_M2_BNL_RC_32828_23.txt', 'ABC130_M2_BNL_RC_32836_4.txt',  'ABC130_M2_BNL_RC_32870_3.txt',
               'ABC130_M2_BNL_RC_32832_10.txt', 'ABC130_M2_BNL_RC_32867_5.txt',  'ABC130_M2_BNL_RC_32870_30.txt',
               'ABC130_M2_BNL_RC_32832_5.txt',  'ABC130_M2_BNL_RC_32869_7.txt',  'ABC130_M2_BNL_RC_32870_40.txt',
               'ABC130_M2_BNL_RC_32835_6.txt',  'ABC130_M2_BNL_RC_32870_27.txt']

LBNL_Results = ['ABC130_M1_LBNL_RC_32909_3.txt', 'ABC130_M1_LBNL_RC_32912_3.txt', 'ABC130_M1_LBNL_RC_32913_4.txt',
                'ABC130_M1_LBNL_RC_32910_3.txt', 'ABC130_M1_LBNL_RC_32912_8.txt', 'ABC130_M1_LBNL_RC_32925_3.txt',

                'ABC130_M2_LBNL_RC_32909_3.txt', 'ABC130_M2_LBNL_RC_32912_3.txt', 'ABC130_M2_LBNL_RC_32913_4.txt',
                'ABC130_M2_LBNL_RC_32910_3.txt', 'ABC130_M2_LBNL_RC_32912_8.txt', 'ABC130_M2_LBNL_RC_32925_3.txt']

SCIPP_Results = ['ABC130_SCIPP01_PXH3_RC_32878_31.txt',
                 'ABC130_SCIPP01_PXH3_RC_32878_34.txt',
                 'ABC130_SCIPP01_PXH3_RC_32878_44.txt',
                 'ABC130_SCIPP01_PXH3_RC_32878_7.txt',

                 'ABC130_SCIPP01_PXH4_RC_32878_31.txt',
                 'ABC130_SCIPP01_PXH4_RC_32878_34.txt',
                 'ABC130_SCIPP01_PXH4_RC_32878_44.txt',
                 'ABC130_SCIPP01_PXH4_RC_32878_7.txt',

                 'ABC130_SCIPP_M7_Hyb2_RC_32929_3.txt',
                 'ABC130_SCIPP_M7_Hyb2_RC_32929_8.txt',
                 'ABC130_SCIPP_M7_Hyb4_RC_32929_8.txt',
                 'ABC130_SCIPP_M7_Hyb4_RC_32929_3.txt']

print(BNL_Results)
print(LBNL_Results)
print(SCIPP_Results)
