import networkx as nx
import matplotlib.pyplot as plt

class SNetworkx:
    
    def __init__(self):
        self.G = nx.Graph()
    
    def inputData(self, source, destionations):
        # topic node
        self.G.add_node(source)
        # reasons nodes
        for each in destionations:
            self.G.add_node(each) #[('slow': 5)]
    
        # adding edges
        for i in range(len(destionations)):
            self.G.add_edge(source, destionations[i], length = 2)
                
                
                
    def show(self):
        nx.draw(self.G, node_size=None, with_labels = True)
        plt.show()