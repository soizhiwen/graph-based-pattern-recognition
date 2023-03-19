#######################
#
# Name: Soi Zhi Wen
# Matriculation Number: 22-132-245
#
# Name:
# Matriculation Number:
#
#######################

import networkx as nx
import numpy as np

import utils

# You can potentially add more code here (constants, functions, ...)


def _ullman_recursive(g1: nx.Graph, g2: nx.Graph, mapping: dict, inverse_mapping: dict, g1_vertices: list, g2_vertices: list) -> bool:
    """
    Recursive part of the Ullman's algorithm

    Returns:
        True if g1 is a subgraph of g2 and False otherwise
    """
    # Code here
    if len(mapping) == len(g1_vertices):
        return True

    for u in g1_vertices:
        if u not in mapping:
            break

    for v in g2_vertices:
        if v not in inverse_mapping:
            break
        elif inverse_mapping[v] is not None:
            continue

        is_match = True
        for u_adj in g1.neighbors(u):
            v_adj = mapping.get(u_adj)
            if v_adj is not None and not g2.has_edge(v, v_adj):
                is_match = False
                break

        if is_match:
            mapping[u] = v
            inverse_mapping[v] = u
            if _ullman_recursive(g1, g2, mapping, inverse_mapping, g1_vertices, g2_vertices):
                return True
            del mapping[u]
            inverse_mapping[v] = None

    return False


def Ullman(g1: nx.Graph, g2: nx.Graph) -> bool:
    """
    Perform the subgraph isomorphism test between g1 and g2

    Args:
        g1: A networkx graph object
        g2: A networkx graph object

    Returns:
        True if g1 is a subgraph of g2 and False otherwise
    """
    # Code here
    # Sort the vertices by degree for faster processing
    g1_vertices = sorted(g1.nodes(), key=lambda x: g1.degree(x), reverse=True)
    g2_vertices = sorted(g2.nodes(), key=lambda x: g2.degree(x), reverse=True)

    mapping = {}
    inverse_mapping = {v: None for v in g2_vertices}
    return _ullman_recursive(g1, g2, mapping, inverse_mapping, g1_vertices, g2_vertices)


if __name__ == "__main__":
    # 1. Load the graphs in the './graphs' folder
    graphs = utils.load_all_graphs("./graphs")

    # 1.5 (You can visualize the graphs using utils.draw_all_graphs())
    # utils.draw_all_graphs(graphs, "./drawings", False)

    # 2. Perform the Ullman's subgraph isomorphic test between all pairs of graphs.
    n = 6
    M = np.zeros((n, n), dtype=int)

    for i, g1 in enumerate(graphs):
        for j, g2 in enumerate(graphs):
            if Ullman(g1, g2):
                M[i][j] = 1

    np.savetxt("./results/ullman_subgraph_isomorphism.csv", M, fmt="%i", delimiter=",")
