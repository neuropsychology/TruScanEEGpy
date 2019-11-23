TruScanEEGpy
============

    
    
.. image:: https://img.shields.io/pypi/v/TruScanEEGpy.svg
        :target: https://pypi.python.org/pypi/TruScanEEGpy

.. image:: https://img.shields.io/travis/neuropsychology/TruScanEEGpy.svg
        :target: https://travis-ci.org/neuropsychology/TruScanEEGpy

.. image:: https://codecov.io/gh/neuropsychology/TruScanEEGpy/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/neuropsychology/TruScanEEGpy
  
.. image:: https://img.shields.io/pypi/dm/TruScanEEGpy
        :target: https://pypi.python.org/pypi/TruScanEEGpy

.. image:: https://readthedocs.org/projects/truscaneegpy/badge/?version=latest
        :target: https://truscaneegpy.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


**Utility functions to work with Deymed's TruScan EEG system.**



Installation
------------

To install TruScanEEGpy, run this command in your terminal:

.. code-block:: console

    $ pip install TruScanEEGpy


Documentation
--------------

.. code-block:: python

    > import TruScanEEGpy
    > import mne
    > 
    > layout = TruScanEEGpy.layout_128('10-5')
    > montage = TruScanEEGpy.montage_mne_128(layout)
    > mne.viz.plot_montage(montage)

.. image:: docs/img/montage_128.png
