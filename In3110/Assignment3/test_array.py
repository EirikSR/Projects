import Array as a
import pytest

test = "er"
shape = (3,)
shape2 = (2, 2)
shape3 = (3, 3)
margin = 1e-10
"""
Tests are parametrized
Tests are mostly for 1D and 2D, an aditional 3D addition test is included to test functionality
Array class was constructed directly with multidimentional support, and tests for 2D used to test
the functionality, since the logic follows for all higher dimentional arrays
"""


def test_string():
    assert isinstance(a.Array(shape, 1, 2, 3).__str__(), str) == True


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [(a.Array(shape, 3, 2, 5), a.Array(shape, 3, 2, 1)), [6, 4, 6]],
        [(a.Array(shape, 4, 2, 2), a.Array(shape, 2, 1, 3)), [6, 3, 5]],
        [(a.Array(shape, 6, 6, 7), a.Array(shape, 4, 0, 2)), [10, 6, 9]],
        [(a.Array(shape2, 4, 2, 2, 2), a.Array(shape2, 1, 2, 1, 3)), [[5, 4], [3, 5]]],
        [(a.Array(shape2, 6, 6, 7, 3), a.Array(shape2, 1, 4, 0, 2)), [[7, 10], [7, 5]]],
        [
            (
                a.Array(shape3, 1, 2, 3, 2, 1, 2, 3, 2, 1),
                a.Array(shape3, 3, 2, 1, 4, 3, 2, 1, 3, 2),
            ),
            [[4, 4, 4], [6, 4, 4], [4, 5, 3]],
        ],
    ],
)
def test_add(arg, expected_output):
    assert arg[0] + arg[1] == expected_output


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [(a.Array(shape, 3, 2, 5), a.Array(shape, 3, 2, 1)), [0, 0, 4]],
        [(a.Array(shape, 4, 2, 2), a.Array(shape, 2, 1, 3)), [2, 1, -1]],
        [(a.Array(shape, 6, 6, 7), a.Array(shape, 4, 0, 2)), [2, 6, 5]],
        [(a.Array(shape2, 4, 2, 2, 2), a.Array(shape2, 1, 2, 1, 3)), [[3, 0], [1, -1]]],
        [(a.Array(shape2, 6, 6, 7, 3), a.Array(shape2, 1, 4, 0, 2)), [[5, 2], [7, 1]]],
    ],
)
def test_sub(arg, expected_output):
    assert arg[0] - arg[1] == expected_output


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [(a.Array(shape, 3, 2, 5), 2), [6, 4, 10]],
        [(a.Array(shape, 4, 2, 2), a.Array(shape, 2, 1, 3)), [8, 2, 6]],
        [(a.Array(shape, 6, 6, 7), -1), [-6, -6, -7]],
        [(a.Array(shape2, 4, 2, 2, 2), a.Array(shape2, 1, 2, 1, 3)), [[4, 4], [2, 6]]],
        [(a.Array(shape2, 6, 6, 7, 3), a.Array(shape2, 1, 4, 0, 2)), [[6, 24], [0, 6]]],
        [(a.Array(shape2, 6, 5, 7, 3), 2), [[12, 10], [14, 6]]],
    ],
)
def test_mul(arg, expected_output):
    assert (arg[0] * arg[1]) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [(a.Array(shape, 3, 2, 5), a.Array(shape, 3, 2, 5)), True],
        [(a.Array(shape, 4, 2, 2), a.Array(shape, 2, 1, 3)), False],
        [(a.Array(shape, 6, 6, 7), a.Array(shape, 6, 6, 7)), True],
        [(a.Array(shape2, 4, 2, 2, 2), a.Array(shape2, 1, 2, 1, 3)), False],
        [(a.Array(shape2, 6, 6, 7, 3), a.Array(shape2, 6, 6, 7, 3)), True],
    ],
)
def test_equal(arg, expected_output):
    assert (arg[0] == arg[1]) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [(a.Array(shape, 3, 2, 5), a.Array(shape, 3, 2, 5)), [True, True, True]],
        [(a.Array(shape, 4, 2, 2), a.Array(shape, 2, 2, 3)), [False, True, False]],
        [(a.Array(shape, 6, 6, 7), 6), [True, True, False]],
        [
            (a.Array(shape2, 4, 2, 2, 2), a.Array(shape2, 1, 2, 2, 3)),
            [False, True, True, False],
        ],
        [(a.Array(shape2, 6, 6, 7, 3), 6), [True, True, False, False]],
    ],
)
def test_isequal(arg, expected_output):
    assert arg[0].is_equal(arg[1]) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [a.Array(shape, 3, 2, 4), 3],
        [a.Array(shape, 4, 2, 2), 8.0 / 3],
        [a.Array(shape, 6, 6, 7), 19.0 / 3],
        [a.Array(shape2, 4, 2, 2, 2), 10.0 / 4],
        [a.Array(shape2, 6, 6, 7, 3), 22.0 / 4],
    ],
)
def test_mean(arg, expected_output):
    assert arg.mean() - expected_output < margin


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [a.Array(shape, 3, 2, 4), 0.66666666666667],
        [a.Array(shape, 4, 2, 2), 0.88888888888889],
        [a.Array(shape, 6, 6, 7), 0.22222222222222],
        [a.Array(shape2, 4, 2, 2, 2), 0.75],
        [a.Array(shape2, 6, 6, 7, 3), 2.25],
    ],
)
def test_variance(arg, expected_output):
    assert arg.variance() - expected_output < 1e-8


@pytest.mark.parametrize(
    "arg, expected_output",
    [
        [a.Array(shape, 3, 2, 4), 2],
        [a.Array(shape, 4, 2, 2), 2],
        [a.Array(shape, 6.0, 6.1, 7.1), 6.0],
        [a.Array(shape2, 4, 2, 1, 2), 1],
        [a.Array(shape2, 6, 6, 7, 3), 3],
    ],
)
def test_min_element(arg, expected_output):
    assert arg.min_element() - expected_output < 1e-8
