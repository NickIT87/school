from ..mymodule import abs_mod
import sys

def test_abs_mod_should_return_positive_number():
    assert abs_mod(-sys.maxsize) == sys.maxsize


def test_abs_mod_should_return_zero_number():
    assert abs_mod(0) == 0


def test_abs_mod_positive_number_from_negative_arg():
    assert abs_mod(1) == 1