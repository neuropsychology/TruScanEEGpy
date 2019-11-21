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
## This function aims to convert the channel labeling (in number) to the standardized 10-20 electrode labeling
#
#def convert_channelnumber_tenfive(channel):
##    channel = layout["Name"]
#    correspondance2 = {
#            "65" : "Fpz",
#            "1" : "FP1",
#            "2" : "FP2",
#
#            "66" : "?66",
#            "67" : "?67",
#
#            "33" : "AF7",
#            "34" : "?34",
#            "68" : "AFz",
#            "36" : "?36",
#            "38" : "AF8",
#
#            "69" : "?69",
#            "70" : "?70",
#            "71" : "?71",
#            "72" : "?72",
#
#            "3" : "F7",
#            "41" : "F5",
#            "4" : "F3",
#            "43" : "F1",
#            "5" : "Fz",
#            "46" : "F2",
#            "6" : "F4",
#            "48" : "F6",
#            "7" : "F8",
#
#            "73" : "?73",
#            "74" : "?74",
#            "75" : "?75",
#            "76" : "?76",
#            "77" : "?77",
#            "78" : "?78",
#            "79" : "?79",
#            "80" : "?80",
#            "81" : "?81",
#            "82" : "?82",
#
#            "50" : "FT9",
#            "51" : "FT7",
#            "20" : "FC5",
#            "35" : "FC3",
#            "21" : "FC1",
#            "83" : "FCz",
#            "22" : "FC2",
#            "39" : "FC4",
#            "23" : "FC6",
#            "40" : "FT8",
#            "44" : "FT10",
#
#            "84" : "?84",
#            "85" : "?85",
#            "86" : "?86",
#            "87" : "?87",
#            "88" : "?88",
#            "89" : "?89",
#            "90" : "?90",
#            "91" : "?91",
#            "92" : "?92",
#            "93" : "?93",
#
#            #"?" : "T9",
#            "8" : "T7",
#            "45" : "C5",
#            "9" : "C3",
#            "49" : "C1",
#            "10" : "Cz",
#            "42" : "C2",
#            "11" : "C4",
#            "37" : "C6",
#            "12" : "T8",
#            #"?" : "T10",
#
#            "94" : "?94",
#            "95" : "?95",
#            "96" : "?96",
#            "97" : "?97",
#            "98" : "?98",
#            "99" : "?99",
#            "100" : "?100",
#            "101" : "?101",
#
#            "47" : "TP7",
#            "25" : "CP5",
#            "52" : "CP3",
#            "26" : "CP1",
#            "53" : "CPz",
#            "27" : "CP2",
#            "54" : "CP4",
#            "28" : "CP6",
#            "55" : "TP8",
#
#            "102" : "?102",
#            "103" : "?103",
#            "104" : "?104",
#            "105" : "?105",
#            "106" : "?106",
#            "107" : "?107",
#            "108" : "?108",
#            "109" : "?109",
#            "110" : "?110",
#            "111" : "?111",
#
#            "13" : "P7",
#            "56" : "P5",
#            "14" : "P3",
#            "57" : "P1",
#            "15" : "Pz",
#            "58" : "P2",
#            "16" : "P4",
#            "59" : "P6",
#            "17" : "P8",
#
#            "24" : "TP9 or P9",
#            "29" : "TP10 or P10",
#
#            "112" : "?112",
#            "113" : "?113",
#            "114" : "?114",
#            "115" : "?115",
#            "116" : "?116",
#            "117" : "?117",
#            "118" : "?118",
#            "119" : "?119",
#
#            "31" : "PO9",
#            "60" : "PO7",
#            "61" : "?61",
#            "62" : "POz",
#            "63" : "?63",
#            "64" : "PO8",
#            "32" : "PO10",
#
#            "120" : "?120",
#            "121" : "?121",
#            "122" : "?122",
#            "123" : "?123",
#
#            "18" : "O1",
#            "30" : "Oz",
#            "19" : "O2",
#
#            "124" : "?124",
#            "125" : "?125",
#
#            "126" : "I1",
#            "127" : "Iz",
#            "128" : "I2"
#            }
#    channel = [correspondance2.get(name, name)  for name in channel]
#    return(channel)
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
