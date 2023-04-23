from utils import load_all_graphs
import networkx as nx


def PMST(graph: nx.Graph):
    # Code here
    # Select an arbitrary starting node
    start_node = list(graph.nodes())[0]

    # Initialize variables
    visited = {start_node}
    unvisited = set(graph.nodes()) - visited
    mst = []

    # Loop until all nodes are visited
    while unvisited:
        min_edge_weight = float('inf')
        min_edge = None
        min_node = None

        # For each visited node
        for v in visited:
            # Find the minimum weight edge connecting it to an unvisited node
            for u in unvisited:
                if graph.has_edge(v, u):
                    edge_weight = graph[v][u]['weight']
                    if edge_weight < min_edge_weight:
                        min_edge_weight = edge_weight
                        min_edge = (v, u)
                        min_node = u

        # Add the minimum weight edge to the MST
        mst.append(min_edge)

        # Add the newly visited node to the visited set
        visited.add(min_node)

        # Remove the newly visited node from the unvisited set
        unvisited.remove(min_node)

    return mst


def ex4():
    graphs = load_all_graphs('./graphs')

    mst = PMST(graphs[-1])

    with open('./results/spanning_tree.txt', 'w') as f:
        for edge in mst:
            f.write(f"({edge[0]}, {edge[1]})\n")


if __name__ == '__main__':
    ex4()
