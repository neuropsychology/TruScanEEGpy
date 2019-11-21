import pytest
import doctest
import TruScanEEGpy


if __name__ == '__main__':
    doctest.testmod()
    pytest.main()


def layout_128():
    assert len(TruScanEEGpy.layout_128().index) == 128
