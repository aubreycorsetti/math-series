from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series


def test_fibonacci0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci11():
    actual = fibonacci(11)
    expected = 89
    assert actual == expected


def test_lucas0():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas1():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas11():
    actual = lucas(11)
    expected = 199
    assert actual == expected


def test_sum_series_f0():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_sum_series_f1():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_sum_series_f11():
    actual = sum_series(11)
    expected = 89
    assert actual == expected


def test_sum_series_l0():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected


def test_sum_series_l1():
    actual = sum_series(1, 2, 1)
    expected = 1
    assert actual == expected


def test_sum_series_l11():
    actual = sum_series(11, 2, 1)
    expected = 199
    assert actual == expected
