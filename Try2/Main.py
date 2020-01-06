from Graph_Creator import *
from helper_foo import *

# PARAMETERS
n_nodes = 6  # Number of countries = number of nodes in a graph
number_of_edges, graph_list = craete_world(n_nodes)  # create iran map
population_size = 4 # number of initial population
muniationRate = 0.2
n_generations = 180 #  times
number_of_parents_to_keep = 1  # In each generation update a certain number of random parents is kept

# MAIN ALGORITHM
input_population = generate_random_initial_population(population_size, n_nodes, graph_list) # return a list of choromosome as inital population

results_fitness, results_fittest = evolution(input_population, n_generations, population_size,
                                             number_to_keep=number_of_parents_to_keep, muniationRate = muniationRate)
# VISUALIZE
visualize_results(results_fitness, results_fittest, n_generations)
plt.show()
