from ..mymodule import abs_mod


def test_abs_mod_should_return_positive_number():
    assert abs_mod(-2) == 2


def test_abs_mod_should_return_zero_number():
    assert abs_mod(0) == 0


def test_abs_mod_should_return_positive_number_from_negative_arg():
    assert abs_mod(1) == 1