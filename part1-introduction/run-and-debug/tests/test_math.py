from src.math import add_two_numbers, diff_two_numbers, mult_two_numbers


def test_add_two_numbers():
    assert add_two_numbers(5, 2) == 7


def test_diff_two_numbers():
    assert diff_two_numbers(6, 3) == 3


def test_mult_two_numbers():
    assert mult_two_numbers(3, 4) == 12
