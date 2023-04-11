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
    def __init__(
        self,
        N,
        crossover_rate,
        mutation_rate,
        iterations,
        crossover_type="PMX",
        mutation_type="EM",
    ):
        self.N = N
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.iterations = iterations
        self.crossover_type = crossover_type
        self.mutation_type = mutation_type
        self.population = None

    def create_initial_population(self, n):
        """Create initial population"""
        self.population = [np.eye(n)[np.random.permutation(n)] for _ in range(self.N)]

    def evaluate_fitness(self, A_1, A_2):
        """evaluate fitness of each individual in the population"""
        return [fitness_func(A_1, A_2, P) for P in self.population]

    def selection(self, fitness_scores):
        """select individuals to breed"""
        sorted_indices = np.argsort(fitness_scores)
        return [self.population[i] for i in sorted_indices[: self.N // 2]]

    def crossover(self, parents):
        """Crossover"""
        offspring = []
        for _ in range(self.N - len(parents)):
            parent1, parent2 = random.sample(parents, 2)
            if random.random() < self.crossover_rate:
                if self.crossover_type == "PMX":
                    child = self.pmx(parent1, parent2)
                else:
                    raise ValueError(f"Invalid crossover type: {self.crossover_type}")
            else:
                child = random.choice(parents).copy()
            offspring.append(child)
        return parents + offspring

    def mutation(self, population):
        """mutate individuals in the population"""
        for individual in population:
            if random.random() < self.mutation_rate:
                if self.mutation_type == "EM":
                    self.exchange_mutation(individual)
                else:
                    raise ValueError(f"Invalid mutation type: {self.mutation_type}")
        return population

    def pmx(self, parent1, parent2):
        size = parent1.shape[0]
        p1, p2 = np.random.randint(0, size, 2)
        if p1 > p2:
            p1, p2 = p2, p1
        child = np.zeros_like(parent1)
        child[p1:p2] = parent1[p1:p2]

        for i in range(p1, p2):
            if not np.any(parent2[i] == child):
                idx = np.where(parent1 == parent2[i])[0][0]
                while p1 <= idx < p2:
                    idx = np.where(parent1 == parent2[idx])[0][0]
                child[idx] = parent2[i]

        for i in range(size):
            if np.all(child[i] == 0):
                child[i] = parent2[i]

        return child

    def exchange_mutation(self, individual):
        i, j = random.sample(range(individual.shape[0]), 2)
        individual[[i, j]] = individual[[j, i]]

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
        self.create_initial_population(A_1.shape[0])
        for _ in range(self.iterations):
            fitness_scores = self.evaluate_fitness(A_1, A_2)
            parents = self.selection(fitness_scores)
            self.population = self.crossover(parents)
            self.population = self.mutation(self.population)

        best_fitness_idx = np.argmin(fitness_scores)
        return fitness_scores[best_fitness_idx], self.population[best_fitness_idx]


def ex3_b():
    # Set random seed
    random.seed(42)
    np.random.seed(42)

    # 1. load the data
    g1, g2 = load_all_graphs("./data/")
    A_1 = nx.adjacency_matrix(g1).toarray()
    A_2 = nx.adjacency_matrix(g2).toarray()

    # 2. Run the Genetic algorithm on the adjacency matrices of the data
    # 2.1 Tweak the parameters of the genetic algorithm to obtain a fitness score <= 4.0
    ga = GeneticAlgorithm(N=100, crossover_rate=0.8, mutation_rate=0.2, iterations=1000)
    score, best_permutation = ga.run(A_1, A_2)

    print(f"Fitness Score: {score}")
    print(f"Best Permutation Matrix:\n{best_permutation}")

    # The fitness score of your solution has to be <= 4.0
    assert score <= 4.0


if __name__ == "__main__":
    ex3_b()
