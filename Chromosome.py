from Graph import *
from City import * 

class Chromosome:
    def __init__(self):
        self.graph = []
        self.__set_map()

    def __set_map(self):
        graph = Graph()

        west_azarbaijan = City("West_Azarbaijan")
        east_azarbaijan = City("East_Azarbaijan")
        ardabil= City("Ardabil")
        kurdestan = City("Kurdestan")
        zanjan = City("Zanjan")
        gilan = City("Gilan")

      
        graph.add_node(west_azarbaijan)
        graph.add_node(east_azarbaijan)
        graph.add_node(ardabil)
        graph.add_node(kurdestan)
        graph.add_node(zanjan)
        graph.add_node(gilan)

        graph.add_edges(west_azarbaijan, [east_azarbaijan, kurdestan, zanjan])
        graph.add_edges(east_azarbaijan, [ardabil, zanjan])
        graph.add_edges(ardabil, [gilan, zanjan])
        graph.add_edges(kurdestan, [zanjan])
        graph.add_edges(zanjan, [gilan])
        self.graph = graph

    def fitness_function(self):
        m = 0
        sum = 0
        for node in self.graph.nodes:
            m += len(node.get_edges())
            for des in node.get_edges():
                sum += self.sigma(node.color , des.color)   
        return sum / m
    
    def sigma(self, src, des):
        return 0 if src == des else 1 

    def __str__(self):
        return self.graph.__str__()