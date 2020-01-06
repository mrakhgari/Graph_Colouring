import networkx as nx
import random
import matplotlib.pyplot as plt  # Drawing graphs


west_azarbaijan = "West_Azarbaijan"
east_azarbaijan = "East_Azarbaijan"
ardabil= "Ardabil"
kurdestan = "Kurdestan"
zanjan = "Zanjan"
gilan = "Gilan"

colours = ['g', 'r', 'y', 'b']

class word_Map:

    def __init__(self):
        self.graph = nx.Graph()
        self.graph.add_node(west_azarbaijan, color = random.choice(colours))
        self.graph.add_node(east_azarbaijan, color = random.choice(colours))
        self.graph.add_node(ardabil, color = random.choice(colours))
        self.graph.add_node(kurdestan, color = random.choice(colours))
        self.graph.add_node(zanjan, color = random.choice(colours))
        self.graph.add_node(gilan, color = random.choice(colours))

        self.graph.add_edges_from([(west_azarbaijan, east_azarbaijan),(west_azarbaijan, kurdestan), (west_azarbaijan, zanjan)])
        # self.graph.add_edges(east_azarbaijan, [ardabil, zanjan])
        # self.graph.add_edges(ardabil, [gilan, zanjan])
        # self.graph.add_edges(kurdestan, [zanjan])
        # self.graph.add_edges(zanjan, gilan)

    def __str__(self):
        nx.draw_networkx(self.graph, with_labels=True, node_color=colours, edge_color=colours)
        plt.draw()
        text = ""
        print (self.graph.edges())
        for city in self.graph:
            text += str(self.graph.adj(city)) + " "
        return text