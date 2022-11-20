import part1
import pytest

def test_exp_decay():
    part1_test = part1.ExponentialDecay(0.4)
    with pytest.raises(AssertionError):
        c = 1
        assert part1_test(c, 3.2) == -1.24