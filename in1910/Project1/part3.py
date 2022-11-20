import numpy as np

class DoublePendulum():
    def __init__(self, m1=1, l1=1, m2=1, l2=1):
        self.m1 = m1
        self.l1 = l1 
        self.m2 = m2 
        self.l2 = l2 

    def __call__(self, t, u):
        """ u[0] is theta1, u[1] is omega1, u[2] is theta2, u[3] is omega2 """
        m1 = self.m1
        l1 = self.l1
        m2 = self.m2
        l2 = self.l2
        # TODO add complicated functions in STUFF
        return np.array([
            u[1], 
            "stuff", 
            u[3], 
            "stuff"
        ])