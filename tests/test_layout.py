import pytest
import doctest
import TruScanEEGpy


if __name__ == '__main__':
    doctest.testmod()
    pytest.main()


def test_channel_names_128():
    assert len(TruScanEEGpy.channel_names_128()) == 128
