import numpy as np
from matplotlib import pyplot as plt


class ChaosGame:
    def __init__(self, n, r):
        """
        Initiating the class
        Args:
            n (int): Number of corners in n-gon
            r (float): Fractal parameter
        Variables initiated:
            Corners (list): Will store the corners of the n-gon
            points (list): Will store points generated within the n-gon
            colors (list): will store list of colors used for plotting
            gradient (list): Will store list of colors as [r, g, b] entries
        """
        self.n = n
        self.r = r
        self.corners = []
        self.points = []
        self.colors = []
        self.gradient = []

    def _generate_ngon(self):
        """
        Function finds last points in N-gon
        Args:
            self: variables inside the class
        Returns:
            Updated corners to hade n-entries of corners

        """
        for i in range(1, self.n + 1):
            ci = (
                np.sin(i * ((2 * np.pi) / self.n)),
                np.cos(i * ((2 * np.pi) / self.n)),
            )
            self.corners.append(np.array(ci))

    def _starting_point(self):
        """
        Function finds a random startpoint within a triangle and returns is
        Args:
            self: variables inside the class
        Returns:
            point (touple) Point is returned as a numpy array
        """
        weights = np.random.dirichlet(np.ones(self.n), size=1)

        point = [0, 0]
        for c, w in zip(self.corners, weights[0]):
            point[0] += c[0] * w
            point[1] += c[1] * w
        return np.array(point)

    def itterate(self, steps, discard=5):
        """
        Function finds X next points within a N-gon given a random start point, returnes list of points
        Args:
            self: variables inside the class
            steps (int): how many itterations used
            discard (int): How many of the first points are discarded
        Returns:
            Updated points, color and gradient lists within the class
        """
        start = self._starting_point()
        rgb = True
        X_past = start

        C = np.array([0, 0, 0])

        vectors = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

        for i in range(0, steps + discard):
            rand_int = np.random.randint(0, self.n)
            corner = self.corners[rand_int]
            X = self.r * X_past + (1 - self.r) * corner

            # FIX FIX FIX
            C = (C + vectors[(rand_int % 3)]) / 2

            if i > discard:
                self.points.append(np.array(X))
                self.gradient.append(C)
                if rgb:
                    self.colors.append(rand_int)
            X_past = X

    def plot(self, color=False, cmap="jet", output="test_chaos.png"):
        """
        Function plots the points stored in the class
        Args:
            self: variables inside the class
            color (bool): Wether to apply collor or use standard (black)
            cmap (plt arg): Specify what matplotlib color map is used
            output (str): String for filename for plot to be saved to

        """
        fig, ax = plt.subplots()
        # ax.scatter(*zip(*self.corners), s=0.1)
        if color:
            color = self.gradient
        else:
            color = "black"
        ax.scatter(*zip(*self.points), s=0.1, c=color, cmap=cmap)
        ax.set_xlim((-2, 2))
        ax.set_ylim((-2, 2))
        x0, x1 = ax.get_xlim()
        y0, y1 = ax.get_ylim()
        ax.set_aspect(abs(x1 - x0) / abs(y1 - y0))
        # ax.grid(b=True, which="major", color="k", linestyle="--")
        fig.savefig(output, dpi=600)

        # Needs to be removed:
        plt.close(fig)

    def show(self, color=False, cmap="jet", output="test_chaos"):
        self.plot(color, cmap, output)
        plt.show()

    """
    Pytest functions below, used to get data stored in class:

    """

    def get_ngon(self):
        return self.corners

    def get_points(self):
        return self.points

    def get_gradient(self):
        return self.gradient

    def _print_corners(self):
        print(self.corners)


if __name__ == "__main__":

    C = ChaosGame(3, 1.0 / 2)
    C._generate_ngon()
    C._print_corners()

    """
    #Testing starting points
    for i in range(1000):
        a = C._starting_point()
        C._add_point(a)
    """
    C.itterate(10000, 5)

    C.show(True, "rainbow")

    n_lst = [3, 4, 5, 5, 6]
    r_lst = [1.0 / 2, 1.0 / 3, 1.0 / 3, 3.0 / 8, 1.0 / 3]
    output = [
        "Chaos1.png",
        "Chaos2.png",
        "Chaos44.png",
        "Chaos4.png",
        "Chaos5.png",
    ]
    for i in range(len(n_lst)):
        C = ChaosGame(n_lst[i], r_lst[i])
        C._generate_ngon()
        C.itterate(10000, 5)
        C.show(True, "rainbow", output[i])
