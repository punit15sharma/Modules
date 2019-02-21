#!/usr/bin/env /Users/zschillaci/Software/miniconda3/envs/pyenv/bin/python
import os
import csv
import collections
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

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

global LBL_modules
LBL_modules = [
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
'ABC130_M6_H6_HCC12']

global SCIPP_modules
SCIPP_modules = [
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
'ABC130_M6_Hyb4']

INPUT_DIR = '/Users/zschillaci/BNL/Working/InnerTracker/Modules/input/'
RESULTS_DIR = '/Users/zschillaci/BNL/Working/InnerTracker/Modules/results/'
