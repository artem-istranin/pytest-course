import sys

import pytest


# raise RuntimeError("Module-level setup error")


def test_regular():
    assert True


@pytest.mark.skipif(sys.version_info < (3, 9), reason="requires python3.10 or higher")
def test_example_for_higher_python_versions():
    a = {"a": 1, "b": 2}
    b = {"b": 2, "c": 3}
    assert a | b == {"a": 1, "b": 2, "c": 3}  # merge operator


def bugged_sort_function(input_list):
    return sorted(input_list, key=lambda x: abs(x))  # Incorrect sorting logic


def sorting_with_known_bug(x):
    return sorted(x, key=lambda x: abs(x))


@pytest.mark.xfail(reason="known bug in sorting; keep an eye on it when it will be fixed")
def test_sorting():
    result = sorting_with_known_bug([-1, 2, -3])
    expected_result = [-3, -1, 2]
    assert result == expected_result
