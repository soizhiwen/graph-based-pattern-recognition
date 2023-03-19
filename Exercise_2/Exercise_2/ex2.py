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
    n_nodes_g1 = len(g1.nodes())
    n_nodes_g2 = len(g2.nodes())
    c_mat = np.zeros((n_nodes_g1 + n_nodes_g2, n_nodes_g1 + n_nodes_g2))

    # Compute substitution cost
    for i in range(n_nodes_g1):
        for j in range(n_nodes_g2):
            if g1.nodes[i]["label"] != g2.nodes[j]["label"]:
                c_mat[i, j] = TAU

    # Compute deletion cost
    for i in range(n_nodes_g1):
        j = n_nodes_g1 + g2.number_of_nodes()  # placeholder for deleted node
        for _, _, label in g1.edges(i, data="label"):
            c_mat[i, j] += TAU

    # Compute insertion cost
    for j in range(n_nodes_g2):
        i = n_nodes_g1 + g1.number_of_nodes()  # placeholder for inserted node
        for _, _, label in g2.edges(j, data="label"):
            c_mat[i, j] += TAU

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
    return None


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
    return 0.0


if __name__ == "__main__":
    # 1. Load the graphs
    graphs = utils.load_all_graphs("./graphs")

    # 1.5 (You can visualize the graphs using utils.draw_all_graphs())
    utils.draw_all_graphs(graphs, "./drawings", False)

    # 2. Compute GED between all pairs of graphs.

    # Save the GEDs in './results/GED_results.csv'
    np.savetxt("./results/GED_results.csv", M, fmt="%i", delimiter=",")
