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
from scipy.optimize import linear_sum_assignment

import utils

# Cost for node del, node ins, edge del, and edge ins
TAU = 1.0


# You can potentially add more code here (constants, functions, ...)


def create_c_mat(g1: nx.Graph, g2: nx.Graph) -> np.ndarray:
    """
    This function creates a cost matrix for the BP GED.
    It takes two input graphs, g1 and g2, and returns the cost matrix.

    The cost matrix is used to determine the cost of different transformations between the two input graphs.
    The transformations include substitution of nodes, deletion of nodes, and insertion of nodes.

    Args:
        g1: A networkx graph object
        g2: A networkx graph object

    Returns:
        Matrix C
    """
    # Code here
    n_nodes_g1 = g1.number_of_nodes()
    n_nodes_g2 = g2.number_of_nodes()
    total_n_nodes = n_nodes_g1 + n_nodes_g2
    c_mat = np.zeros((total_n_nodes, total_n_nodes))

    for i, (u1, attrs1) in enumerate(g1.nodes(data=True)):
        for j, (u2, attrs2) in enumerate(g2.nodes(data=True)):
            c_mat[i, j] = np.linalg.norm(attrs1["x"] - attrs2["x"])
        c_mat[i, n_nodes_g2 + i] = TAU  # deletion of node u1

    for j, (u2, attrs2) in enumerate(g2.nodes(data=True)):
        c_mat[n_nodes_g1 + j, j] = TAU  # insertion of node u2

    return c_mat


def augment_c_mat(g1, g2, c_mat) -> np.ndarray:
    """
    Create the augmented matrix C*.
    C* uses the node degree information to encode the local edge structure in Matrix C.

    Args:
        g1: A networkx graph object
        g2: A networkx graph object
        c_mat: Matrix C

    Returns:
        Matrix C*
    """
    # Code here
    n_nodes_g1 = g1.number_of_nodes()
    n_nodes_g2 = g2.number_of_nodes()

    for i, (u1, attrs1) in enumerate(g1.degree):
        for j, (u2, attrs2) in enumerate(g2.degree):
            c_mat[i, j] += np.linalg.norm(attrs1 - attrs2)
        c_mat[i, n_nodes_g2 + i] += attrs1

    for j, (u2, attrs2) in enumerate(g2.degree):
        c_mat[n_nodes_g1 + j, j] += attrs2

    return c_mat


def BP_GED(g1: nx.Graph, g2: nx.Graph) -> float:
    """
    Compute the BP Graph Edit Distance between the two input graphs

    1. Create the C matrix
    2. Create the augmented C matrix C*
    3. Solve the linear sum assignment problem with **scipy.optimize.linear_sum_assignment**
    4. Compute the cost of the node edit operations
    5. Compute the cost of the edges edit operations
    6. Returns the cost of the nodes + cost of the edges

    Args:
        g1: A networkx graph object
        g2: A networkx graph object

    Returns:
        The Graph Edit Distance between g1 and g2
    """
    # Code here
    # 1. Create the C matrix
    c_mat = create_c_mat(g1, g2)

    # 2. Create the augmented C matrix C*
    c_star = augment_c_mat(g1, g2, c_mat)

    # 3. Solve the linear sum assignment problem
    row_ind, col_ind = linear_sum_assignment(c_star)

    # 4. Compute the cost of the node edit operations
    nodes_cost = 0
    for i in range(len(row_ind)):
        if row_ind[i] < g1.number_of_nodes() and col_ind[i] < g2.number_of_nodes():
            nodes_cost += c_star[row_ind[i], col_ind[i]]
        elif row_ind[i] < g1.number_of_nodes() and col_ind[i] >= g2.number_of_nodes():
            nodes_cost += TAU
        elif row_ind[i] >= g1.number_of_nodes() and col_ind[i] < g2.number_of_nodes():
            nodes_cost += TAU

    # 5. Compute the cost of the edge edit operations
    edges_cost = 0
    if g1.edges() != g2.edges():
        edges1 = set(g1.edges())
        edges2 = set(g2.edges())
        common_edges = edges1.intersection(edges2)
        edges_cost += len(edges1 - common_edges)
        edges_cost += len(edges2 - common_edges)

    # 6. Returns the cost of the nodes + cost of the edges
    return nodes_cost + edges_cost


if __name__ == "__main__":
    # 1. Load the graphs
    graphs = utils.load_all_graphs("./graphs")

    # 1.5 (You can visualize the graphs using utils.draw_all_graphs())
    utils.draw_all_graphs(graphs, "./drawings", False)

    # 2. Compute GED between all pairs of graphs.
    n = 5
    D = np.zeros((n, n), dtype=int)

    for i, g1 in enumerate(graphs):
        for j, g2 in enumerate(graphs):
            D[i, j] = BP_GED(g1, g2)

    # Save the GEDs in './results/GED_results.csv'
    np.savetxt("./results/GED_results.csv", D, fmt="%i", delimiter=",")
