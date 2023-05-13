import csv
import os.path

import networkx as nx
from networkx.algorithms import similarity
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

from utils import load_all_graphs
from typing import List


def compute_dissimilarity(graphs: List[nx.Graph]) -> np.ndarray:
    num_graphs = len(graphs)
    D = np.zeros((num_graphs, num_graphs))

    for i in range(num_graphs):
        for j in range(i, num_graphs):
            if i == j:
                continue
            D[i, j] = ged(graphs[i], graphs[j])
            D[j, i] = D[i, j]

    return D


def ged(graph1: nx.Graph, graph2: nx.Graph) -> float:
    # Implementation of graph edit distance algorithm
    return similarity.graph_edit_distance(graph1, graph2, timeout=0.05)


def plot_mds(embedding: np.ndarray, classes: List[int]):
    fig, ax = plt.subplots()
    scatter = ax.scatter(embedding[:, 0], embedding[:, 1], c=classes)
    legend = ax.legend(*scatter.legend_elements(), title="Classes")
    ax.add_artist(legend)
    plt.savefig("./results/plot_mds.png")
    plt.show()


def main():
    # Code Here
    graphs = load_all_graphs("./graphs")
    D = compute_dissimilarity(graphs)
    D = np.nan_to_num(D)

    # Apply MDS to embed the graphs into a 2D plane
    mds = MDS(n_components=2, dissimilarity="euclidean", normalized_stress="auto")
    embedding = mds.fit_transform(D)

    # Load the class labels from the CSV file
    classes = []
    with open("./graphs/classes.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            _, graph_class = row
            graph_class = int(graph_class)
            classes.append(graph_class)

    plot_mds(embedding, classes)


if __name__ == "__main__":
    main()
