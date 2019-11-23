
# TruScanEEGpy

**Utilities to work with Deymed’s TruScan EEG system.**

## Installation

## Documentation

``` python
import TruScanEEGpy
import mne

layout = TruScanEEGpy.layout_128('10-5')
montage = TruScanEEGpy.montage_mne_128(layout)
mne.viz.plot_montage(montage)
```

![](docs/img/unnamed-chunk-2-1.png)<!-- -->
