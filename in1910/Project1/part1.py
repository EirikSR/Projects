from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

class ExponentialDecay():
    def __init__(self, a):
        self.a = a

    def __call__(self, t, u):
        return -self.a*u

    def solve(self, u0, T, dt):
        return integrate.solve_ivp(
            self.__call__, [0, T], u0, t_eval=np.linspace(0, T, T/dt))

if __name__ == "__main__":
    decay_model = ExponentialDecay(0.4)
    solution = decay_model.solve((1, 2, 3, 4), 10, 0.1)
    t = solution.t
    u = solution.y

    for u_ in u:
        plt.plot(t, u_)
    plt.show()



