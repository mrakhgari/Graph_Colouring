# city class, used as nodes in graph
# contains name of city and color

import numpy as np

class City:
    
    def __init__(self, name= 'city'):
        self.__name = name
        self.color = np.random.choice(['r', 'b', 'g', 'y'], 1)
        self.__edges = []

    def __eq__(self, value):
        if isinstance(value, str):
            return self.__name == value
        if not isinstance(value, City):
            return NotImplemented
        else: return self.__name == value.__name
    
    def get_edges(self):
        return self.__edges

    def __repr__(self):
        return "City instanse "
    
    def __str__(self):
        text = "city: " + str(self.__name) + ", color: " + str(self.color) +"\n"
        # for city in self.__edges:
            # text += str(city) + ", "
        return text

    def __hash__(self):
        return hash(self.__name)
    