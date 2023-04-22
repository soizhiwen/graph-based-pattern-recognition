from utils import load_all_graphs
import networkx as nx


def PMST(graph: nx.Graph):
    # Code here

def ex4():
    graphs = load_all_graphs('./graphs')

    PMST(graphs[-1])


if __name__ == '__main__':
    ex4()
