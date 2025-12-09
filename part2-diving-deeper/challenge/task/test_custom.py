from more_itertools import partition, windowed, interleave

# TODO Part 1: Implement your tests here


# TODO Part 2: Add the `rolling_aggregate` function prototype below to `more.py`,
# then implement and test it.

# ⚠️ Warning: Add `'rolling_aggregate'` to the `__all__` list in `more.py`.
# If you skip this step, the test will fail with:
# ImportError: cannot import name 'rolling_aggregate' from 'more_itertools'

'''
def rolling_aggregate(seq, window_size, agg_fn):
    """
    Apply a rolling aggregation over a sequence using a custom aggregation function.

    Parameters:
        seq: Input sequence of data.
        window_size: Size of each rolling window (number of elements).
        agg_fn: Aggregation function to apply to each window (e.g., sum, mean).

    Return:
        tuple: (position, result), where `position` is the index in `seq` and `result` is the
        output of `agg_fn` applied to the current window.
    """
    pass
'''

# Optional (for better IDE navigation and autocompletion):
# To expose `rolling_aggregate` in the type stubs, add it to `__all__` in the `more.pyi` file
# and copy the following interface definition there:
'''
def rolling_aggregate(
    seq: Iterable[_T],
    window_size: int,
    agg_fn: Callable[[Iterable[_T]], _U],
) -> Iterator[tuple[int, _U]]: ...
'''
