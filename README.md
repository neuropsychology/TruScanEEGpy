
# TruScanEEGpy

[![pypi](https://img.shields.io/pypi/v/TruScanEEGpy.svg)](https://pypi.python.org/pypi/TruScanEEGpy)
[![Build
Status](https://img.shields.io/travis/neuropsychology/TruScanEEGpy.svg)](https://travis-ci.org/neuropsychology/TruScanEEGpy)
[![codecov](https://codecov.io/gh/neuropsychology/TruScanEEGpy/branch/master/graph/badge.svg)](https://codecov.io/gh/neuropsychology/TruScanEEGpy)
[![Documentation
Status](https://readthedocs.org/projects/truscaneegpy/badge/?version=latest)](https://truscaneegpy.readthedocs.io/en/latest/?badge=latest)

**Utilities to work with Deymed’s TruScan EEG system.**

## Installation

To install TruScanEEGpy, run this command in your terminal:

    pip install https://github.com/neuropsychology/TruScanEEGpy/zipball/master

## Documentation

``` python
import TruScanEEGpy
import mne

layout = TruScanEEGpy.layout_128('10-5')
montage = TruScanEEGpy.montage_mne_128(layout)
mne.viz.plot_montage(montage)
```

![](docs/img/unnamed-chunk-2-1.png)<!-- -->
