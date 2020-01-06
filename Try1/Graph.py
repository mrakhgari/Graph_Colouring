class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def add_edges(self, node, edges):
        if node not in self.nodes:
            self.add_node(node)
        self.nodes[self.nodes.index(node)].get_edges().extend(edges)
        for des in edges:
            if des not in self.nodes:
                self.add_node(des)
            self.nodes[self.nodes.index(des)].get_edges().append(node)

    def get_adj(self, node):
        return self.nodes[self.nodes.index(node)].get_edges()

    def __str__(self):
        text = ""
        for city in self.nodes:
            text += str(city)
            text += "\n"
        return text