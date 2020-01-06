from Graph import *
from City import * 

west_azarbaijan = "West_Azarbaijan"
east_azarbaijan = "East_Azarbaijan"
ardabil= "Ardabil"
kurdestan = "Kurdestan"
zanjan = "Zanjan"
gilan = "Gilan"


class Chromosome:
    def __init__(self):
        self.graph = self.__set_map()

    def __set_map(self):
        graph = Graph()
      
        graph.add_node(City(west_azarbaijan))
        graph.add_node(City(east_azarbaijan))
        graph.add_node(City(ardabil))
        graph.add_node(City(kurdestan))
        graph.add_node(City(zanjan))
        graph.add_node(City(gilan))

        graph.add_edges(west_azarbaijan, [east_azarbaijan, kurdestan, zanjan])
        graph.add_edges(east_azarbaijan, [ardabil, zanjan])
        graph.add_edges(ardabil, [gilan, zanjan])
        graph.add_edges(kurdestan, [zanjan])
        graph.add_edges(zanjan, [gilan])
        return graph

    def __str__(self):
        return self.graph.__str__()