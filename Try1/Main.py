import numpy as np
from Chromosome import *
import random
from Word_Map import *

chromosomes = []
for _ in range(100):
    chromosomes.append(Chromosome())

def parent_selection(input_population, number_of_pairs):
    fitness_sum = 0
    probabilities =[]
    for chromosome in input_population:
        fitness_sum += chromosome.fitness_function()
    probabilities = np.array([chromosome.fitness_function() / fitness_sum for chromosome in input_population])
    return np.random.choice(input_population, number_of_pairs, p=probabilities).tolist()

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
        first_parnet = input_population[random.randint(0, len(input_population))-1].graph.nodes
        secend_parent = first_parnet
        while first_parnet == secend_parent:
            secend_parent = input_population[random.randint(0, len(input_population)-1)].graph.nodes
        new_chromosomes.extend(crossover(first_parnet, secend_parent))


# select_parent(parent_selection(chromosomes,4))
print(word_Map())