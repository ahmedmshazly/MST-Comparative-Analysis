import networkx as nx
from networkx.algorithms import tree
import matplotlib.pyplot as plt

class KruskalMST:
    def __init__(self, graph):
        self.graph = graph

    def find_mst(self):
        G = nx.Graph()
        for node in self.graph.get_nodes():
            for target, weight in self.graph.edges.get(node, []):
                G.add_edge(node, target, weight=weight)

        mst_edges = tree.minimum_spanning_edges(G, algorithm="kruskal", data=False)
        return list(mst_edges)

    def draw_mst(self):
        G = nx.Graph()
        mst_edges = self.find_mst()
        for edge in mst_edges:
            G.add_edge(edge[0], edge[1])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='blue', node_size=700)
        plt.title("Kruskal's Minimum Spanning Tree")
        plt.show()
