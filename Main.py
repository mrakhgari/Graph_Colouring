import numpy as np
from Chromosome import *
import random

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

def crossover(first, secend):
    random_number = random.randint(0, len(first.graph.nodes))
    # i need sleep :((
    first_ch = Chromosome()
    second_ch = Chromosome()

    first_ch.graph.nodes = first[0:random_number]
    first_ch.graph.nodes.extend(secend[random_number:])

    secend_ch.graph.nodes = secend[0: random_number]
    secend.ch.graph.nodes.extend(first[random_number:])
    return list[first_ch, second_ch]

def select_parent(input_population):
    new_chromosomes = []
    for i in range(len(input_population)):
        first_parnet = np.random.choice(input_population, 1)
        secend_parent = first_parnet
        while first_parnet == secend_parent:
            secend_parent = np.random.choice(input_population, 1)
        new_chromosomes.extend(crossover(first_parnet, secend_parent))


for i in (parent_selection(chromosomes,4)):
    print(i)