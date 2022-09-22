from ..mymodule import something
import sys


def test_something_first_branch():
    assert something(sys.maxsize) == sys.maxsize
    assert type(something(-sys.maxsize)) == int
    assert something(0) == 0
    assert something(1.1) == False


def test_something_second_branch():
    assert something(True) == True
    assert type(something(True)) == bool


def test_something_third_branch():
    assert something("test") == 'set of chars'
    assert type(something("test")) == str


def test_something_fourth_branch():
    assert something(None) == False
    assert type(something(None)) == bool