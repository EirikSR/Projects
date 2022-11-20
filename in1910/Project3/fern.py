import numpy as np
from matplotlib import pyplot as plt


class AffineTransformation:
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        """
        Initiating the class
        Args:
            a, b, c, d, e, f (float): numbers to be added to transformation matrixes

        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self, x, y):
        """
        Function to generate next point in the seried
        Args:
            self: variables inside the class
            x (float): float representing x-coordinates
            y (float): float representing y-coordinates
        Returnes:
            point (touple): New point moved by transformatiopn matrix
        """
        X = np.array([x, y])
        mat = np.array([[self.a, self.b], [self.c, self.d]])
        vec = np.array([self.e, self.f])

        return np.dot(mat, X) + vec


# Initiating the transpormation functions:
f1 = AffineTransformation(0, 0, 0, 0.16, 0, 0)
f2 = AffineTransformation(0.85, 0.04, -0.04, 0.85, 0, 1.6)
f3 = AffineTransformation(0.2, -0.26, 0.23, 0.22, 0, 1.6)
f4 = AffineTransformation(-0.15, 0.28, 0.26, 0.24, 0, 0.44)

lst = [[1, 1]]

# Itterating 50000 times, using if-statements to detemine what transformation will be applied
for i in range(50000):
    r = np.random.random()
    if r < 0.01:
        lst.append(f1(lst[i][0], lst[i][1]))
    elif r > 0.01 and r < 0.08:
        lst.append(f4(lst[i][0], lst[i][1]))
    elif r > 0.08 and r < 0.15:
        lst.append(f3(lst[i][0], lst[i][1]))
    else:
        lst.append(f2(lst[i][0], lst[i][1]))


# Same plotting technique as used in chaos_game.py
fig, ax = plt.subplots()

ax.scatter(*zip(*lst), s=0.1, color="forestgreen")
ax.set_xlim((-5, 5))
ax.set_ylim((0, 12))
x0, x1 = ax.get_xlim()
y0, y1 = ax.get_ylim()
ax.set_aspect(abs(x1 - x0) / abs(y1 - y0))

fig.savefig("barnsley_fern.png", dpi=600)

plt.close(fig)