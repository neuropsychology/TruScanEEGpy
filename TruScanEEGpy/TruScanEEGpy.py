## -*- coding: utf-8 -*-
#
#"""Main module."""
#
#
#import mne
##import autoreject
#import neurokit as nk
#import pandas as pd
#import numpy as np
#
#
#
## =============================================================================
## Montage
## =============================================================================
#
#
#

#
## Layout
#
#def make_layout():
#    layout = pd.read_csv('deymed_layout_128.txt', sep = '\t')
#    layout.columns = layout.columns.str.strip()
#    layout["Name"] = deymed_128_channel_names()
##    layout["Name"] = convert_channelnumber_tenfive(layout["Name"])
##   layout = layout.iloc[0:64].copy()
##   layout["Name"] = [str(i) for i in layout["ID"].values]
#    layout = layout.set_index('Name')
#    layout = layout.to_dict(orient = "index")
#    for channel in layout.keys():
#        yxz = np.array([layout[channel]["Y"], -1*layout[channel]["X"], layout[channel]["Z"]])
#        layout[channel] = yxz
#    layout = mne.channels.make_dig_montage(layout, coord_frame='head')
#    return(layout)
#
#
## Plot the layouts
#
##plot_2d = mne.viz.plot_montage(layout)
##plot_3d = mne.viz.plot_montage(layout, kind = "3d")
