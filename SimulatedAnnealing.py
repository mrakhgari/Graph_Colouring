import math
import numpy as np
from helper_foo import *
from Graph_Creator import *


class SimulatedAnnealing:
    def __init__(self):
        self.number_of_edges, self.graph_list  = craete_world(6)
        self.current = generate_random_initial_population(1,self.number_of_edges, self.graph_list)[0]

    def simulated_annealing(self, schedule, alpha):
        for t in range(1, int(10000000)):
            T = schedule(1, alpha, t)
            print("T is " + str(T) + " in time " + str(t)) 
            if T == 0: 
                return self.current
            next = self.find_successor()
            print(next)
            dE = next.fitness - self.current.fitness
            if dE > 0 :
                self.current = next
                print("in first if")
            elif np.random.uniform(0, 1) < math.e ** (dE/T):
                self.current = next
                print("in second if")

    def find_successor(self):
        return generate_random_initial_population(1,self.number_of_edges, self.graph_list)[0]
