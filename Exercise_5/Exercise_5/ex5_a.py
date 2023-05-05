import networkx as nx
import numpy as np

from utils import load_all_graphs, draw_all_graphs


def shortest_path_kernel(s1: nx.Graph, s2: nx.Graph) -> float:
    # Code here
    # Compute shortest paths between all pairs of nodes in each graph
    sp1 = dict(nx.all_pairs_shortest_path_length(s1))
    sp2 = dict(nx.all_pairs_shortest_path_length(s2))

    # Compute the kernel using the shortest-path lengths
    kernel = 0.0
    for u in s1.nodes():
        for v in s1.nodes():
            if u == v:
                continue
            for u_prime in s2.nodes():
                for v_prime in s2.nodes():
                    if u_prime == v_prime:
                        continue
                    kernel += np.exp(-0.5 * (sp1[u][v] - sp2[u_prime][v_prime]) ** 2)

    return kernel


def main():
    graphs = load_all_graphs("./graphs")

    draw_all_graphs(graphs, "./drawings", False)

    n = len(graphs)
    K = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            K[i, j] = shortest_path_kernel(graphs[i], graphs[j])
            K[j, i] = K[i, j]

    # Apply the Floyd-Warshall algorithm to compute all-pair shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if K[i, j] > K[i, k] + K[k, j]:
                    K[i, j] = K[i, k] + K[k, j]

    np.savetxt("./results/SPK_results.csv", K, fmt="%f", delimiter=",")


if __name__ == "__main__":
    main()
