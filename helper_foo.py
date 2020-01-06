import matplotlib.pyplot as plt  # Drawing graphs
import numpy as np
import random
import networkx as nx

colours = ['r', 'g', 'b', 'y']


class Choromosome:
    def __init__(self, colors, adjacency_list):
        self.colors = colors  # colors of cities, a string with values 'r','b','g','y'
        self.adjacency_list = adjacency_list 
        self.n_nodes = len(self.colors)
        self.fitness, self.graph_nx = self.__convert_to_nxgraph(self.colors, self.adjacency_list)

    def __convert_to_nxgraph(self, colors, adjacency_list):
        G = nx.Graph()
        sum = 0
        m = 0 # number_of_edges_twice
        for index, node_color in enumerate(colors):
            G.add_node(index, color=node_color)
            if index < len(adjacency_list):
                m += len(adjacency_list[index])
                for neighbour in adjacency_list[index]:
                    G.add_edge(index, neighbour) 
                    sum += self.__sigma(node_color ,colors[neighbour])  # set fitness 
        return sum / m , G
    
    def __sigma(self, src, des):
        return 0 if src == des else 1 
                

    def print_graph(self, figure_number=-1, figure_title=''):
        colors_nodes = [element[1]['color'] for element in self.graph_nx.nodes(data= True)]     
        plt.figure(figure_number)
        plt.title(figure_title)
        nx.draw_networkx(self.graph_nx, with_labels=True, node_color=colors_nodes)
        plt.draw()

    def __str__(self):
        return self.colors.__str__() + str(self.fitness)

def parent_selection(input_population, number_of_pairs):
    input_n = len(input_population)
    
    fitness_sum = sum([person.fitness for person in input_population])
    probabilities = np.array([person.fitness / fitness_sum for person in input_population])
    Ixs = []
    Iys = []

    for i in range(input_n):
        I_x = np.random.choice(np.arange(0, input_n), 1, p=probabilities)[0]
        I_y = I_x
        while I_y == I_x:
            I_y = np.random.choice(np.arange(0, input_n), 1, p=probabilities)[0]
        Ixs.append(I_x)
        Iys.append(I_y)
    return [(input_population[Ixs[i]], input_population[Iys[i]]) for i in range(number_of_pairs)]


def mutation(node):
    n_nodes = node.n_nodes
    node1 = np.random.randint(0, n_nodes)
    
    mapper = {'r': ['b', 'y','g'], 'b': ['r','y' ,'g'], 'g': ['r','y', 'b'], 'y' :['b','g','r']}

    child_one_colors = node.colors

    child_one_colors = child_one_colors[:node1] + np.random.choice(mapper[child_one_colors[node1]],
                                                                    1)[0] + child_one_colors[node1 + 1:]
    return child_one_colors


# Define a genetic operator
def genetic_operator(pair_of_parents, method='SPC'):

    n_nodes = pair_of_parents[0].n_nodes
    al = pair_of_parents[0].adjacency_list

    # Step 1) Select a random point
    # Step 2) All colours to the left will be from parent 1, all parent to the right are from parent 2
    point = np.random.randint(0, n_nodes)
    parent_1_colors = pair_of_parents[0].colors
    parent_2_colors = pair_of_parents[1].colors
    child_one_colors = []
    child_one_colors = parent_1_colors[:point] + parent_2_colors[point:]
    child_two_colors = parent_2_colors[:point] + parent_1_colors[point:]
    
    return (Choromosome(child_one_colors, al), Choromosome(child_two_colors, al))


# Population update
def population_update(input_population, output_population_size,
                      number_to_keep=1, muniationRate = 0.2):

    input_population_size = len(input_population)
    output_population = []

    input_population.sort(key=lambda x: x.fitness, reverse=True)
    input_population = input_population[:int(input_population_size / number_to_keep)]
      
    list_of_parent_pairs = parent_selection(input_population, input_population_size // 2)

    pair_index = 0
    while pair_index < len(list_of_parent_pairs):
        child_1, child_2 = genetic_operator(list_of_parent_pairs[pair_index])
        output_population.append(child_1)
        output_population.append(child_2)
        pair_index += 1

    for i in range(int (muniationRate * output_population_size * output_population[0].n_nodes)):
        ran = random.randint(0, len(output_population)-1)
        output_population[ran].colors = mutation(output_population[ran])
    
    return output_population


# Generate random initial population
def generate_random_initial_population(population_size, n_nodes, graph):
    initial_population = []
    
    # Generate random initial population
    for _ in range(population_size):
        color_list = np.random.choice(colours,n_nodes) # colored cities 
        color_string = "".join(color_list)
        initial_population.append(Choromosome(color_string, graph))
    
    return initial_population


# Find fittest
def find_fittest(input_population):
    fitness_list = [person.fitness for person in input_population]
    ix = np.argmax(fitness_list)
    return fitness_list, ix, input_population[ix]


# Roll the evolution
def evolution(input_population, n_generations, population_size, number_to_keep=1, muniationRate = 0.2):
    results_fitness = []
    results_fittest = []

    for i in range(n_generations):
        fitness_list, ix, fittest_coloring = find_fittest(input_population)
        results_fitness.append(fitness_list)
        results_fittest.append(fittest_coloring)
        # Print highest fitness
        print('The fittest person is: ' + str(max(fitness_list)))
        if fitness_list[ix] == 1:
            return results_fitness, results_fittest

        # Update
        output_population = population_update(input_population, population_size, number_to_keep=number_to_keep, muniationRate = muniationRate)
        input_population = output_population
        

    return results_fitness, results_fittest


# Visualize results
def visualize_results(results_fitness, results_fittest, number_of_generations_to_visualize=3):
    # Important
    total_generations = len(results_fitness)

    # Pick generations to visualize
    I = list(
        np.random.choice(list(range(1, total_generations - 1)), number_of_generations_to_visualize - 2))
    I += [0, total_generations - 1]
    I.sort()
    print("Visualized generations: ",end='')
    print(I)

    # Main
    for i, order in enumerate(I):
        results_fittest[order].print_graph(figure_number=i,
                                        figure_title='generation: ' + str(order + 1) + ', fitness: ' + str(
                                            results_fittest[order].fitness))
        plt.draw()
