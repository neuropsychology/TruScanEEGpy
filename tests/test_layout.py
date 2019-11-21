import pytest
import doctest
import TruScanEEGpy


if __name__ == '__main__':
    doctest.testmod()
    pytest.main()


def layout_128():
    assert len(TruScanEEGpy.layout_128(names = "10-5").index) == 128
