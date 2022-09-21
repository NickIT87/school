from ..mymodule import something


def test_something_first_branch():
    assert something(12) == 12
    assert type(something(12)) == int


def test_something_second_branch():
    assert something(True) == True
    assert type(something(True)) == bool


def test_something_third_branch():
    assert something("test") == 'set of chars'
    assert type(something("test")) == str


def test_something_fourth_branch():
    assert something(None) == False
    assert type(something(None)) == bool