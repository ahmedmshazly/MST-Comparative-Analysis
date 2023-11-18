import networkx as nx
from networkx.algorithms import tree

class PrimMST:
    def __init__(self, graph):
        self.graph = graph

    def find_mst(self):
        # Convert the graph to a NetworkX graph for using Prim's algorithm
        G = nx.Graph()
        for node in self.graph.get_nodes():
            for target, weight in self.graph.edges.get(node, []):
                G.add_edge(node, target, weight=weight)

        # Use NetworkX to find the minimum spanning tree using Prim's algorithm
        mst_edges = tree.minimum_spanning_edges(G, algorithm="prim", data=False)
        return list(mst_edges)
