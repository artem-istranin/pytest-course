from more_itertools import partition, windowed, interleave, rolling_aggregate
import pytest


class TestPartition:
    def test_happy_path(self):
        is_odd = lambda x: x % 2 != 0
        iterable = range(10)
        even_items, odd_items = partition(is_odd, iterable)
        actual_even_items = list(even_items)
        actual_odd_items = list(odd_items)

        expected_even_items = [0, 2, 4, 6, 8]
        expected_odd_items = [1, 3, 5, 7, 9]

        assert actual_even_items == expected_even_items
        assert actual_odd_items == expected_odd_items

    def test_different_values(self):
        iterable = [0, 1, False, True, '', ' ']
        false_items, true_items = partition(None, iterable)
        actual_false_items = list(false_items)
        actual_true_items = list(true_items)

        expected_false_items = [0, False, '']
        expected_true_items = [1, True, ' ']

        assert actual_false_items == expected_false_items
        assert actual_true_items == expected_true_items

    def test_partition_raises_error_if_not_iterable(self):
        not_iterable = 123
        with pytest.raises(TypeError):
            partition(None, not_iterable)


class TestWindowed:
    def test_happy_path(self):
        windowed_iter = windowed(seq=range(5), n=2, fillvalue=None, step=1)
        actual_slices = list(windowed_iter)
        expected_slices = [(0, 1), (1, 2), (2, 3), (3, 4)]
        assert actual_slices == expected_slices

    def test_step_two(self):
        windowed_iter = windowed(seq=range(5), n=2, fillvalue=None, step=2)
        actual_slices = list(windowed_iter)
        expected_slices = [(0, 1), (2, 3), (4, None)]
        assert actual_slices == expected_slices

    def test_window_size_is_equal_to_input_iter(self):
        windowed_iter = windowed(seq=range(10), n=10, fillvalue=None, step=2)
        actual_slices = list(windowed_iter)
        expected_slices = [tuple(range(10))]
        assert actual_slices == expected_slices


class TestIterleave:
    def test_happy_path(self):
        interleave_iter = interleave(range(1, 3), range(100, 1005), range(-5, 90000000))
        actual_res = list(interleave_iter)
        expected_res = [1, 100, -5, 2, 101, -4]
        assert actual_res == expected_res

    def test_single_input_iter(self):
        interleave_iter = interleave(range(10))
        actual_res = list(interleave_iter)
        expected_res = list(range(10))
        assert actual_res == expected_res

    def test_floats(self):
        # range(1, 6) -> [1, 2, 3, 4, 5]
        # 0.1 * x -> [0.1, 0.2, 0.3, 0.4, 0.5]
        interleave_iter = interleave((0.1 * x for x in range(1, 6)))
        actual_res = list(interleave_iter)
        expected_res = [0.1, 0.2, 0.3, 0.4, 0.5]
        assert actual_res == pytest.approx(expected_res)


class TestRollingAgg:
    def test_identity(self):
        agg_res = rolling_aggregate(range(5), window_size=3, agg_fn=lambda x: x)
        actual_agg_res = list(agg_res)
        expected_agg_res = [(0, (0, 1, 2)), (1, (1, 2, 3)), (2, (2, 3, 4))]
        assert actual_agg_res == expected_agg_res

    def test_sum(self):
        agg_res = rolling_aggregate(range(5), window_size=3, agg_fn=sum)
        actual_agg_res = list(agg_res)
        expected_agg_res = [(0, 3), (1, 6), (2, 9)]
        assert actual_agg_res == expected_agg_res

    def test_mean_aggregation(self):
        def mean_function(inputs):
            return sum(inputs) / len(list(inputs))

        rolling_iter = rolling_aggregate(seq=range(0, 10, 2), window_size=3, agg_fn=mean_function)
        actual_output = list(rolling_iter)
        expected_output = [(0, 2.0), (1, 4.0), (2, 6.0)]

        for (actual_index, actual_agg_res), (expected_index, expected_agg_res) in zip(actual_output, expected_output):
            assert actual_index == expected_index
            assert actual_agg_res == pytest.approx(expected_agg_res)


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
    window_seq = windowed(seq, window_size)
    for i, x in enumerate(window_seq):
        yield i, agg_fn(x)
'''
