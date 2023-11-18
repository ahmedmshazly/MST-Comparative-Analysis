class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, node1, node2, weight):
        self.add_node(node1)
        self.add_node(node2)
        self.edges.setdefault(node1, []).append((node2, weight))
        self.edges.setdefault(node2, []).append((node1, weight))

    def get_nodes(self):
        return self.nodes

    def get_edges(self):
        return self.edges
