from fuel import convert
from fuel import gauge
import pytest

def main():
    test_convert()
    test_gauge()
    return 0

def test_convert():
    assert convert('1/4') == 25

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value_error():
    with pytest.raises(ValueError):
        convert('t/a')

def test_gauge():
    assert gauge(25) == '25%'
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'

if __name__ == "__main__":
    main()