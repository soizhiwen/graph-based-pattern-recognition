#######################
#
# Name: Soi Zhi Wen
# Matriculation Number: 22-132-245
#
# Name:
# Matriculation Number:
#
#######################


from typing import List

import networkx as nx
import numpy as np
import os
import itertools

from utils import load_graph, draw_graph, COLOR_MAP, NODE_LABEL


#################
#    Part 1     #
#################


def part1() -> List[nx.Graph]:
    """
    1. Load all the graphs in './graphs'
    2. Plot and save the corresponding graph drawing in './drawings'
    3. Return the list of loaded graphs

    Returns:
        The list of loaded graphs
    """
    # Code here
    graphs = []
    basepath = "./graphs"

    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_file():
                graph = load_graph(entry.path)
                name = entry.name.removesuffix(".graphml")
                filename = f"./drawings/{name}.png"
                num_nodes = graph.number_of_nodes()
                labels = dict(list(NODE_LABEL.items())[:num_nodes])
                node_color = list(COLOR_MAP.values())[:num_nodes]
                draw_graph(graph, filename, labels, node_color, nx.spring_layout)
                graphs.append(graph)
    return graphs


#################
#    Part 2     #
#################


def naive_graph_isomorphism(graph1: nx.Graph, graph2: nx.Graph) -> bool:
    """
    This function checks if two input graphs are isomorphic
    by comparing the number of nodes, number of edges and the labels of the nodes.

    Args:
        graph1: A networkx graph object
        graph2: A networkx graph object

    Returns:
        Returns True if the input graphs are isomorphic, else False.
    """
    # Code here
    if graph1.number_of_nodes() != graph2.number_of_nodes():
        return False
    if graph1.number_of_edges() != graph2.number_of_edges():
        return False
    if list(graph1.nodes) != list(graph2.nodes):
        return False
    return True


def part2(graphs: List[nx.Graph]) -> None:
    """
    1. Complete 'naive_graph_isomorphism(graph1, graph2)'
    2. Construct an NxN matrix in which each element represents
       the result of the isomorphic test between two graphs.
       The value at the intersection of row i and column j indicating
       whether the i-th and j-t graphs are isomorphic.
    3. Save the NxN matrix in './results/naive_isomorphic_test.csv'

    Args:
        graphs: A list of networkx graph objects

    """
    # Code here
    is_isomorphism = []
    for graph1, graph2 in itertools.combinations_with_replacement(graphs, 2):
        is_isomorphism.append(naive_graph_isomorphism(graph1, graph2))

    n = 5
    m = np.zeros((n, n), dtype=int)
    for i in range(0, n):
        m[i][i:] = is_isomorphism[: n - i]
        is_isomorphism = is_isomorphism[n - i :]

    m = m + m.T - np.diag(np.diag(m))
    np.savetxt("./results/naive_isomorphic_test.csv", m, fmt="%i", delimiter=",")


def main():
    # Run part 1
    graphs = part1()

    # Run part 2
    part2(graphs)


if __name__ == "__main__":
    main()
