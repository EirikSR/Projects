from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt


class pendulum:
    def __init__(self, M=1, L=1):
        self.M = M
        self.L = L

    def __call__(self, t, y0):
        x1 = y0[0]
        x2 = y0[1]

        dtx1_dt = x2
        dtx2_dt = (-9.81 / self.L) * np.sin(x1)
        # print((x1, x2))
        return (dtx1_dt, dtx2_dt)

    def solve(self, y0, T, dt):
        self.solution = integrate.solve_ivp(
            self.__call__, [0, T], y0, t_eval=np.linspace(0, T, T / dt)
        )
        print(self.solution.t)
        # t = self.solution.t
        # self.tetha = self.solution.y[0]
        # self.omega = self.solution.y[1]
        plt.plot(self.solution.y[1])
        # plt.show()

    @property
    def t(self):
        try:
            return self.solution.t
        except:
            raise Exception("Solve function not yet called")

    @property
    def tetha(self):
        try:
            return self.solution.y[0]
        except:
            raise Exception("Solve function not yet called")

    @property
    def omega(self):
        try:
            return self.solution.y[1]
        except:
            raise Exception("Solve function not yet called")


if __name__ == "__main__":
    test = pendulum(1, 2.7)
    print(test(0.01, (np.pi / 6, 0.15)))
    ret = test.solve((np.pi / 6, 0.15), 1, 0.01)
    print(test.omega)
