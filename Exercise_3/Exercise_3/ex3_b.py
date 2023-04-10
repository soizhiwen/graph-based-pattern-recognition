import networkx as nx
import numpy as np
import random

from utils import load_all_graphs, draw_all_graphs


def fitness_func(A_1: np.ndarray, A_2: np.ndarray, P: np.ndarray) -> float:
    """
    Compute the fitness score F(P) = ||A_1P - PA_2||_2^2

    Args:
        A_1: Adjacency matrix of graph 1
        A_2: Adjacency matrix of graph 2
        P: Permutation matrix

    Returns:
        Fitness score of the given permutation matrix

    """
    return np.linalg.norm(A_1 @ P - P @ A_2, ord=2) ** 2


class GeneticAlgorithm:

    def __init__(self, ...):
        pass

    def create_initial_population(self, ...):
        """Create initial population"""
        pass

    def evaluate_fitness(self, ...):
        """evaluate fitness of each individual in the population"""
        pass

    def selection(self, ...):
        """select individuals to breed"""
        pass

    def crossover(self, ...):
        """Crossover"""
        pass

    def mutation(self, ...):
        """mutate individuals in the population"""
        pass

    def run(self, A_1: np.ndarray, A_2: np.ndarray) -> (float, np.ndarray):
        """
        Run the genetic algorithm to find the isomoprhism (permutation matrix P)
        between the adjacency matrices of graph 1 and graph 2.

        Args:
            A_1: Adjacency matrix of graph 1
            A_2: Adjacency matrix of graph 2

        Returns:
            A tuple with the fitness score of the best permutation matrix and the corresponding permutation matrix.
        """
        return 0, None


def ex3_b():
    # Set random seed
    random.seed(42)
    np.random.seed(42)

    # 1. load the data

    # 2. Run the Genetic algorithm on the adjacency matrices of the data
    # 2.1 Tweak the parameters of the genetic algorithm to obtain a fitness score <= 4.0

    # The fitness score of your solution has to be <= 4.0
    assert score <= 4.0


if __name__ == '__main__':
    ex3_b()
