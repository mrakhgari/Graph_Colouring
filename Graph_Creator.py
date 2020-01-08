import networkx as nx  # Generating of graphs


# list of cities
west_azarbaijan = 0
east_azarbaijan = 1
ardabil= 2
kurdestan = 3
zanjan = 4
gilan = 5
Kermanshah = 6
Hamedan = 7 
Qazvin = 8
Mazandaran = 9
Golestan = 10
Ilam = 11
Lorestan = 12
Markazi = 13
Alborz = 14 
Tehran = 15
Khuzestan = 16
ChaharmahalAndBakhriari = 17
Isfahan = 18
Qom = 19
Semnan = 20
NorthKhorasan = 21
RazaviKhorasan = 22
SouthKhorasan = 23
Yazd = 24
Kerman = 25
Fars = 26
Bushehr = 27
Hormozgan = 28
SistanAndBaluchestan = 29
KohgiluyehAndBoyer = 30


def craete_world(number_of_nodes):    
    G = nx.Graph()
    # add cities
    for i in range(number_of_nodes):
        G.add_node(i)

    G.add_edges_from([(west_azarbaijan, east_azarbaijan),(west_azarbaijan, kurdestan), (west_azarbaijan, zanjan)])
    G.add_edges_from([(east_azarbaijan, ardabil) ,(east_azarbaijan, zanjan)])
    G.add_edges_from([(ardabil, gilan), (ardabil, zanjan)])
    G.add_edges_from([(kurdestan, zanjan), (kurdestan, Kermanshah), (kurdestan, Hamedan) ])
    G.add_edges_from([(zanjan, gilan), (zanjan, Qazvin), (zanjan, Hamedan)])
    G.add_edges_from([(kurdestan, Hamedan), (kurdestan, Kermanshah)])
    G.add_edges_from([(Kermanshah, Hamedan), (Kermanshah, Ilam), (Kermanshah, Lorestan)])
    G.add_edges_from([(Ilam, Lorestan), (Ilam, Khuzestan)])
    G.add_edges_from([(Lorestan, Khuzestan), (Lorestan, ChaharmahalAndBakhriari), (Lorestan, Markazi), (Lorestan, Hamedan), (Lorestan, Isfahan)])
    G.add_edges_from([(Hamedan, Qazvin), (Hamedan, Markazi)])
    G.add_edges_from([(Qazvin, Alborz),(Qazvin, Mazandaran), (Qazvin, Markazi)])
    G.add_edges_from([(Markazi, Qom),(Markazi, Tehran), (Markazi, Alborz), (Markazi, Isfahan)])
    G.add_edges_from([(Alborz, Tehran), (Alborz, Markazi)])
    G.add_edges_from([(Mazandaran, Golestan), (Mazandaran, Semnan)])
    G.add_edges_from([(Golestan, NorthKhorasan), (Golestan, Semnan)])
    G.add_edges_from([(NorthKhorasan,RazaviKhorasan), (NorthKhorasan,Semnan)] )
    G.add_edges_from([(Semnan, RazaviKhorasan), (Semnan, SouthKhorasan), (Semnan, Isfahan), (Semnan, Qom)])
    G.add_edges_from([(Qom, Isfahan)])
    G.add_edges_from([(Khuzestan, ChaharmahalAndBakhriari),(Khuzestan, KohgiluyehAndBoyer), (Khuzestan, Bushehr)])
    G.add_edges_from([(Isfahan,ChaharmahalAndBakhriari), (Isfahan, SouthKhorasan), (Isfahan, Yazd), (Isfahan, Fars), (Isfahan, KohgiluyehAndBoyer) ])
    G.add_edges_from([(ChaharmahalAndBakhriari, KohgiluyehAndBoyer )])
    G.add_edges_from([(KohgiluyehAndBoyer, Fars), (KohgiluyehAndBoyer, Bushehr)])
    G.add_edges_from([(Yazd, SouthKhorasan), (Yazd, Kerman), (Yazd, Fars)])
    G.add_edges_from([(Fars, Bushehr), (Fars, Kerman), (Fars, Hormozgan)])
    G.add_edges_from([(Bushehr, Hormozgan)])
    G.add_edges_from([(Hormozgan, Kerman), (Hormozgan, SistanAndBaluchestan)])
    G.add_edges_from([(Kerman, SouthKhorasan), (Kerman, SistanAndBaluchestan)])
    G.add_edges_from([(SouthKhorasan, SistanAndBaluchestan)])
    G.add_edges_from([(gilan, Mazandaran), (gilan, Qazvin)])
    # a list of edges, with index: city and value: neighbors 
    edges = []
    for i in range(number_of_nodes):
        edges.append(list(G.adj[i].keys()))
    return G.number_of_edges(), edges