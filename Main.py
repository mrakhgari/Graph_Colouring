from Graph_Creator import *
from helper_foo import *

# PARAMETERS
n_nodes = 31  # Number of countries = number of nodes in a graph
number_of_edges, graph_list = craete_world(n_nodes)  # create iran map
population_size = 100 # number of initial population
muniationRate = 0.1
n_generations = 500 #  times
tornumentSize = 2 # In each generation update a certain number of random parents is kept

# MAIN ALGORITHM
input_population = generate_random_initial_population(population_size, n_nodes, graph_list) # return a list of choromosome as inital population

for i in input_population:
    print(i)

results_fitness, results_fittest, res= evolution(input_population, n_generations, population_size,
                                             number_to_keep=tornumentSize, muniationRate = muniationRate)
# VISUALIZE
visualize_results(results_fitness, results_fittest,res, 3)
plt.show()
