from part2 import pendulum
import pytest
import numpy as np

test = pendulum(1, 2.7)
"""

@pytest.mark.parametrize(
    "try_", [(test.t, True), (test.tetha, True), (test.omega, True)]
)"""


def test_array_exception_t():
    # print(try_)
    try:
        test.t
        b = False
    except Exception:
        b = True
    assert b


def test_array_exception_tetha():
    # print(try_)
    try:
        test.tetha
        b = False
    except Exception:
        b = True
    assert b


def test_array_exception_omega():
    # print(try_)
    try:
        test.omega
        b = False
    except Exception:
        b = True
    assert b


margin = 0.0001


def test_call():
    a, b = test(0.01, (np.pi / 6, 0.15))
    assert a - 0.15 < margin and b - 1.8167e-2 < margin


# test_array_exception()
test_call()