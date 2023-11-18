from graph import Graph
from kruskal import KruskalMST
from prim import PrimMST

def create_graph():
    edges = {
        'a': [('f', 5), ('l', 14), ('c', 8)],
        'b': [('k', 47), ('f', 20), ('d', 8), ('h', 12)],
        'c': [('a', 8), ('i', 10), ('g', 12), ('l', 8)],
        'd': [('g', 22), ('f', 94), ('b', 8)],
        'e': [('l', 15), ('i', 16), ('h', 8)],
        'f': [('k', 16), ('a', 5), ('i', 8), ('d', 94), ('b', 20)],
        'g': [('l', 13), ('c', 12), ('j', 5), ('d', 22)],
        'h': [('j', 16), ('e', 8), ('l', 15), ('b', 12)],
        'i': [('f', 8), ('c', 10), ('e', 16)],
        'j': [('k', 5), ('g', 5), ('h', 16)],
        'k': [('j', 5), ('b', 47), ('f', 16)],
        'l': [('h', 15), ('e', 15), ('c', 8), ('a', 14), ('g', 13)],
    }

    graph = Graph()
    for node, links in edges.items():
        for target, weight in links:
            graph.add_edge(node, target, weight)
    return graph

def main():
    graph = create_graph()

    # Kruskal's Algorithm
    kruskal_mst = KruskalMST(graph)
    kruskal_edges = kruskal_mst.find_mst()
    print("Kruskal's MST:", kruskal_edges)

    # Prim's Algorithm
    prim_mst = PrimMST(graph)
    prim_edges = prim_mst.find_mst()
    print("Prim's MST:", prim_edges)

if __name__ == "__main__":
    main()
