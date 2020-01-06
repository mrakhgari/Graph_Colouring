import networkx as nx  # Generating of graphs


# list of cities
west_azarbaijan = 0
east_azarbaijan = 1
ardabil= 2
kurdestan = 3
zanjan = 4
gilan = 5


def craete_world(number_of_nodes):    
    G = nx.Graph()
    G.add_node(west_azarbaijan)
    G.add_node(east_azarbaijan)
    G.add_node(ardabil)
    G.add_node(kurdestan)
    G.add_node(zanjan)
    G.add_node(gilan)

    G.add_edges_from([(west_azarbaijan, east_azarbaijan),(west_azarbaijan, kurdestan), (west_azarbaijan, zanjan)])
    G.add_edges_from([(east_azarbaijan, ardabil) ,(east_azarbaijan, zanjan)])
    G.add_edges_from([(ardabil, gilan), (ardabil, zanjan)])
    G.add_edges_from([(kurdestan, zanjan)])
    G.add_edges_from([(zanjan, gilan)])

    # a list of edges, with index: city and value: neighbors 
    edges = []
    for i in range(number_of_nodes):
        edges.append(list(G.adj[i].keys()))
    return G.number_of_edges(), edges