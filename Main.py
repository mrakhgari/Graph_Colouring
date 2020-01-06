import numpy as np
from Chromosome import *

chromosomes = []
for _ in range(100):
    chromosomes.append(Chromosome())

def parent_selection(input_population, number_of_pairs):
    fitness_sum = 0
    probabilities =[]
    for chromosome in input_population:
        fitness_sum += chromosome.fitness_function()
    probabilities = np.array([chromosome.fitness_function() / fitness_sum for chromosome in input_population])
    return np.random.choice(input_population, number_of_pairs, p=probabilities)


for i in (parent_selection(chromosomes,4)):
    print(i)