# -*- coding: utf-8 -*-

"""Submodule."""
import mne
import numpy as np
import pandas as pd


def montage_mne_128(layout):
    """Create MNE montage

    Examples
    --------
    >>> import TruScanEEGpy
    >>> import mne
    >>>
    >>> layout = TruScanEEGpy.layout_128('10-5')
    >>> montage = TruScanEEGpy.montage_mne_128(layout)
    >>> mne.viz.plot_montage(montage)
    >>> mne.viz.plot_montage(montage, kind = "3d")
    >>>
    >>> # Compare to other standard montages
    >>> montage = mne.channels.make_standard_montage('standard_1005')
    >>> montage.get_positions()
    >>> montage.get_positions()['ch_pos']["TP9"]
    >>> mne.viz.plot_montage(montage)
    >>>
    >>> montage = mne.channels.make_standard_montage('biosemi128')
    >>> montage.get_positions()
    >>> mne.viz.plot_montage(montage)
    >>>
    >>> montage = mne.channels.make_standard_montage('GSN-HydroCel-128')
    >>> montage.get_positions()
    >>> mne.viz.plot_montage(montage)
    >>>
    >>> montage = mne.channels.make_standard_montage('easycap-M1')
    >>> mne.viz.plot_montage(montage)
    """
    layout["ID"] = layout["Name"]
    layout = layout.set_index("Name")
    layout = layout.to_dict(orient="index")
    for channel in layout.keys():
        yxz = np.array([layout[channel]["Y"], -1 * layout[channel]["X"], layout[channel]["Z"]])
        layout[channel] = yxz / 1000  # The unit in the deymed layout file is bigger than in MNE

    montage = mne.channels.make_dig_montage(
        layout,
        # standard_1005 -----------
        # nasion=np.array([8.12812462e-06, 8.50133285e-02, -3.91550369e-02]),
        # lpa=np.array([-0.08429365, -0.01957576, -0.04699231]),
        # rpa=np.array([0.08401729, -0.01959495, -0.04703638]),
        # biosemi128 -----------
        # nasion=np.array([5.27205792e-18, 8.60992398e-02, -4.01487349e-02]),
        # lpa=np.array([-0.08609924, -0.0, -0.04014873]),
        # rpa=np.array([0.08609924, 0.0, -0.04014873]),
        # GSN-HydroCel-128 -----------
        nasion=np.array([0.0, 0.09821842, -0.02554916]),
        lpa=np.array([-0.07266855, 0.00043744, -0.03520521]),
        rpa=np.array([0.07266855, 0.00043744, -0.03520521]),
        # TruScanEEGpy -----------
        # nasion=np.array([0.0, 0.08116, -0.03279]),
        # lpa=np.array([-0.07685, 0.02609, -0.03279]),
        # rpa=np.array([0.07685, 0.02609, -0.03279]),
        coord_frame="unknown",  # "unknown",
    )
    return montage
