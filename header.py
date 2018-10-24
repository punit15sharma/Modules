#!/usr/bin/env /Users/zschillaci/Software/miniconda3/envs/pyenv/bin/python
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

recption_dir = '/Users/zschillaci/BNL/Working/StaveAssembly/Modules/input/bnl_reception_test/'
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
'ABC130_M9_Hyb0_RC_0_0.txt',
'ABC130_M9_Hyb6_RC_0_0.txt',
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

production_dir = '/Users/zschillaci/BNL/Working/StaveAssembly/Modules/input/production_site_results/'
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
'ABC130_M9_Hyb0_RC_2_40.txt',
'ABC130_M9_Hyb6_RC_2_40.txt',
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