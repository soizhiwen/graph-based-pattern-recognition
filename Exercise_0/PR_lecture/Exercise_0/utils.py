from typing import Callable, List

import networkx as nx
from matplotlib import pyplot as plt


###############
#  CONSTANTS  #
###############

COLOR_MAP = {
    1.0: "#648FFF",
    2.0: "#785EF0",
    3.0: "#DC267F",
    4.0: "#FE6100",
    5.0: "#FFB000",
    6.0: "#004D40",
    7.0: "#420E00",
}

# NODE_LABEL = "x"
NODE_LABEL = {
    "0": 1.0,
    "1": 2.0,
    "2": 3.0,
    "3": 4.0,
    "4": 5.0,
    "5": 6.0,
    "6": 7.0,
}

###############
#   UTILS     #
###############


def load_graph(filename: str) -> nx.Graph:
    """
    Load the **file.graphml** as a **nx.Graph**.

    Args:
        filename:

    Returns:
        The loaded NetworkX graph
    """
    # Code here
    return nx.read_graphml(filename)


def draw_graph(
    graph: nx.Graph,
    filename: str,
    labels: dict = None,
    node_color: List[str] = None,
    layout: Callable[[nx.Graph], dict] = None,
) -> None:
    """
    This function draws a given networkx graph object, saves the drawing to a specified file

    Args:
        graph: A networkx graph object.
        filename: A string representing the path and filename
                  where the graph will be saved as an image.
        labels: A dictionary that maps node indices to labels.
        node_color: A list of strings representing the color of each node in the graph.
        layout: A layout function that takes a graph as input and returns a dictionary of node positions
                If None, the **nx.kamada_kawai_layout** layout will be used.

    """
    # Code here
    pos = layout(graph, seed=3113794652)
    options = {
        "alpha": 0.9,
        "node_size": 800,
        "edgecolors": "tab:gray",
        "font_color": "whitesmoke",
        "node_color": node_color,
        "labels": labels,
        "with_labels": True,
    }
    nx.draw(graph, pos, **options)
    plt.savefig(filename)
