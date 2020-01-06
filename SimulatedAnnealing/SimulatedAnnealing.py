import math
import numpy as np
from helper. import Choromosome


class SimulatedAnnealing:
    def __init__(self):
        self.current = None

    def simulated_annealing(self, schedule):
        for t in range(1, math.inf):
            T = schedule(t)
            if T is 0: return self.current
            next = np.random.choice(self.current.colors)
            dE = next.fitness - self.current.fitness
            if dE > 0 :
                self.current = next
                print("in first if")
            elif np.random.uniform(0, 1) < math.e ** (dE/T):
                self.current = next
                print("in second if")


    def first_method(self, t0, alpha, k):
        self.
