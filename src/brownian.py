import numpy as np


class Brownian:
    def __init__(self):
        pass

    @staticmethod
    def simulate(sigma, iterations):
        points = [0]
        for i in range(iterations - 1):
            step = np.random.normal(0, sigma)
            points.add(points[i] + step)
