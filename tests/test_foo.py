import pytest
import doctest
import TruScanEEGpy


if __name__ == '__main__':
    doctest.testmod()
    pytest.main()


def test_foo():
    assert TruScanEEGpy.foo() == 4
