from typing import List

import networkx as nx
import numpy as np

from utils import load_all_graphs


# Define a function to count the frequency of a given graphlet in a graph
def count_graphlet(G, H):
    count = 0
    for sub_nodes in nx.subgraph(G, H).nodes():
        subgraph = nx.subgraph(G, sub_nodes)
        if nx.is_isomorphic(subgraph, H):
            count += 1
    return count


def graphlet_kernel(
    graph1: nx.Graph, graph2: nx.Graph, graphlets: List[nx.Graph]
) -> float:
    """

    Args:
        graph1:
        graph2:
        graphlets:

    Returns:

    """
    # Code Here
    # Compute the frequencies of each graphlet in each graph
    frequencies1 = [count_graphlet(graph1, H) for H in graphlets]
    frequencies2 = [count_graphlet(graph2, H) for H in graphlets]

    # Compute the kernel between the two graphs
    kernel = np.dot(frequencies1, frequencies2)
    return kernel


def main():
    # Code Here
    graphs = load_all_graphs("./graphs")
    graphlets = load_all_graphs("./graphlets")

    # Compute the enumerating kernel between all pairs of graphs
    n = len(graphs)
    K = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            K[i, j] = graphlet_kernel(graphs[i], graphs[j], graphlets)
            K[j, i] = K[i, j]

    np.savetxt("./results/EK_results.csv", K, fmt="%i", delimiter=",")


if __name__ == "__main__":
    main()
