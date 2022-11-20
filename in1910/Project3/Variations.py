from chaos_game import ChaosGame
import numpy as np
from matplotlib import pyplot as plt


class Variations:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def swirl(self):
        self.x = x * np.sin(r ** 2) - y * np.cos(r ** 2)
        self.y = x * np.cos(r ** 2) - y * np.sin(r ** 2)

    def get(self):
        return [x, y]


C = ChaosGame(3, 0.5)
C._generate_ngon()
C.itterate(10000, 5)
points = C.get_points()
r = 1
lst = []

grid_values = np.linspace(-1, 1, 10)
x, y = np.meshgrid(grid_values, grid_values)

A = Variations(x, y, "swirl")


ax.scatter(*zip(*lst), s=0.1, color="forestgreen")
ax.set_xlim((-5, 5))
ax.set_ylim((-5, 5))
x0, x1 = ax.get_xlim()
y0, y1 = ax.get_ylim()
ax.set_aspect(abs(x1 - x0) / abs(y1 - y0))

fig.savefig("v1.png", dpi=600)

plt.close(fig)