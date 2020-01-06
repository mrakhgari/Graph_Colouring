import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

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
