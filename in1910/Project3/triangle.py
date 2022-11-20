import numpy as np
from matplotlib import pyplot as plt


def find_triangle(A, B):
    """
    Function finds last point in a equilateral triangle
    Args:
        A (touple): touple of floats, representing a point in 2D plane
        B (touple): same as A
    Returns:
        Triangle (lst): List of 3 touples, representing a triangle in the 2D plane

    """
    dX = B[0] - A[0]
    dY = B[1] - A[1]

    # Determining C by rotating the point B by 60 degrees
    tetha = np.deg2rad(60)
    cX = np.cos(tetha) * dX - np.sin(tetha) * dY + A[0]
    cY = np.sin(tetha) * dX + np.cos(tetha) * dY + A[1]

    C = np.array([cX, cY])
    triangle = [A, B, C]

    return triangle


def plot_lst(lst):
    """
    Function plots a list of points and saves it
    Args:
        lst (list): List of points to be plotted

    """
    fig, ax = plt.subplots()
    ax.scatter(*zip(*lst), s=0.1)
    ax.set_xlim((0, 5))
    ax.set_ylim((0, 5))
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    ax.set_aspect(abs(x1 - x0) / abs(y1 - y0))
    ax.grid(b=True, which="major", color="k", linestyle="--")
    fig.savefig("test.png", dpi=600)
    plt.close(fig)


def plot_rgb(lst, color):
    """
    Function plots a list of points with color and saves it
    Args:
        lst (list): List of points to be plotted
        color (list): List of colors to be usen in conjunction with the list
    """
    red = lst[color == 0]
    green = lst[color == 1]
    blue = lst[color == 2]
    col = ["blue", "green", "red"]
    A = [red, green, blue]
    print(color)
    fig, ax = plt.subplots()
    for i in range(len(A)):
        ax.scatter(*zip(*A[i]), s=0.1, color=col[i])

    ax.set_xlim((0, 5))
    ax.set_ylim((0, 5))
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    ax.set_aspect(abs(x1 - x0) / abs(y1 - y0))
    ax.grid(b=True, which="major", color="k", linestyle="--")
    fig.savefig("test_rgb.png", dpi=600)
    plt.close(fig)


def plot_gradient(lst, color):
    """
    Function plots a list of points with color gradient and saves it
    Args:
        lst (list): List of points to be plotted
        gradient (list): List of colors to be usen in conjunction with the list
    """
    fig, ax = plt.subplots()

    ax.scatter(*zip(*lst), s=0.1, c=color)

    ax.set_xlim((0, 5))
    ax.set_ylim((0, 5))
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    ax.set_aspect(abs(x1 - x0) / abs(y1 - y0))
    ax.grid(b=True, which="major", color="k", linestyle=" ")
    fig.savefig("test_grad.png", dpi=600)
    plt.close(fig)


def find_start_point(triangle):
    """
    Function finds a random startpoint within a triangle and returns is
    Args:
        triangle (list): List of touples representing the corners of the triangle
    Returns:
        point (touple) Point is returned as a numpy array
    """
    weights = np.random.dirichlet(np.ones(3), size=1)

    point = [0, 0]
    for c, w in zip(triangle, weights[0]):
        point[0] += c[0] * w
        point[1] += c[1] * w

    return np.array(point)


def itterate_rand_points(triangle, rgb=True):
    """
    Function finds 10000 next points within a triangle given a random start point, returnes list of points
    Args:
        triangle (list): List of touples representing the corners of the triangle
        rgb (bool): Optional argument, if true, a color list will be constructed
    Returns:
        points (list): List of all generated points
        color(list): List of closest corner, used for plotting colors
    """
    start = find_start_point(triangle)
    ret_lst = []
    X_past = start
    color = []
    for i in range(0, 10000 + 5):
        rand_int = np.random.randint(0, 3)
        corner = triangle[rand_int]
        X = (X_past + corner) / 2

        if i > 5:
            ret_lst.append(np.array(X))
            if rgb:
                color.append(rand_int)
        X_past = X

    return np.array(ret_lst), np.array(color)


def itterate_rand_points_gradient(triangle):
    """
    Function finds 10000 next points within a triangle given a random start point, returnes list of points
    Args:
        triangle (list): List of touples representing the corners of the triangle
    Returns:
        points (list): List of all generated points
        color(list): List of gradiented colors used for plotting
    """
    start = find_start_point(triangle)

    ret_lst = []
    X_past = start
    color = []
    C = np.array([0, 0, 0])

    vectors = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    for i in range(0, 10000 + 5):
        rand_int = np.random.randint(0, 3)
        corner = triangle[rand_int]
        X = (X_past + corner) / 2

        C = (C + vectors[rand_int]) / 2
        if i > 5:
            ret_lst.append(np.array(X))
            color.append(C)

        X_past = X

    return np.array(ret_lst), np.array(color)


A = np.array([0, 3])
B = np.array([3, 0])

lst = find_triangle(A, B)
plot_lst(lst)
itt, col = itterate_rand_points_gradient(lst)
plot_gradient(itt, col)
# print(col)
# print(itt)
# plot_rgb(itt, col)
