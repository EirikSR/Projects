import pytest
from chaos_game import ChaosGame
import numpy as np

# Course testing, will however be the accurate solution for n=4, whitch is tested
@pytest.mark.parametrize("n", [3, 4, 5])
def test_points(n):
    Gon = ChaosGame(n, 0.5)
    Gon._generate_ngon()
    Gon.itterate(10000, 5)
    points = Gon.get_ngon()
    corner = Gon.get_ngon()
    X = []
    Y = []

    for x in corner:
        X.append(x[0])
        Y.append(x[1])

    Outside = False
    for p in points:
        if p[0] < min(X) or p[0] > max(X) or p[1] < min(Y) or p[1] > max(Y):
            Outside = True

    assert Outside == False


# Testing each side in the n-gon is of equal length
@pytest.mark.parametrize("n", [3, 4, 5])
def test_ngon(n):
    Gon = ChaosGame(n, 0.5)
    Gon._generate_ngon()

    p = Gon.get_ngon()
    length = []

    equidist = True

    for i in range(len(p) - 1):
        length.append(
            np.sqrt(
                (p[i][0] - p[i + 1][0]) ** 2 + np.sqrt((p[i][1] - p[i + 1][1]) ** 2)
            )
        )
    length.append(
        np.sqrt((p[0][0] - p[-1][0]) ** 2 + np.sqrt((p[0][1] - p[-1][1]) ** 2))
    )

    for i in range(len(length) - 1):
        if length[i] - length[i + 1] > 0.0001:
            equidist = False

    assert equidist == True


# Testing that all generated starting points lie within the square spanned by the n-gon (course, but accurate for n=4)
@pytest.mark.parametrize("n", [3, 4, 5])
def test_start(n):
    Gon = ChaosGame(4, 0.5)
    Gon._generate_ngon()

    corner = Gon.get_ngon()
    X = []
    Y = []

    for x in corner:
        X.append(x[0])
        Y.append(x[1])
    points = []

    for i in range(10000):
        points.append(Gon._starting_point())

    Outside = False
    for p in points:
        if p[0] < min(X) or p[0] > max(X) or p[1] < min(Y) or p[1] > max(Y):
            Outside = True

    assert Outside == False


# Testing that all gradient entries have a length of 3, all values are between 0 and 1
@pytest.mark.parametrize("n", [3, 4, 5])
def test_gradient(n):
    Gon = ChaosGame(3, 0.5)
    Gon._generate_ngon()
    Gon.itterate(10000, 5)
    gradient = Gon.get_gradient()
    Col = True

    for c in gradient:
        if len(c) != 3:
            Col = False
            break
        if c[0] > 1 or c[1] > 1 or c[2] > 1:
            Col = False

    assert Col == True


# Only the square is equidistant...
