from ..mymodule import UEFA_practice


test_data = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_negative():
    assert UEFA_practice(test_data[0]) == False


def test_first_m():
    assert UEFA_practice(test_data[1]) == "Іспанія"
    assert UEFA_practice(test_data[2]) == "Іспанія"
    assert UEFA_practice(test_data[5]) == "Іспанія"


def test_second_m():
    assert UEFA_practice(3) == "Німеччина"
    assert UEFA_practice(7) == "Німеччина"


def test_third_s():
    assert UEFA_practice(4) == "Англія"
    assert UEFA_practice(9) == "Англія"
    assert UEFA_practice(10) == "Англія"


def test_fourth_t():
    assert UEFA_practice(6) == "Португалія"
    assert UEFA_practice(8) == "Португалія"


