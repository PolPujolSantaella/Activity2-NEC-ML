import math
import random
import numpy as np

from src.chromosome import Individual
from src.fitness import evaluate_fitness
from src.genetic_operators import single_gene_mutation


def simulated_annealing(graph, max_colors, initial_temp=1000, cooling_rate=0.99, max_iters=5000):
    """
    Simulated Annealing for graph coloring problem
    """

    num_nodes = graph.number_of_nodes()
    edges_array = np.array(graph.edges()) - 1

    # Initialize solution
    current_ind = Individual(num_nodes, max_colors)
    current_fitness = evaluate_fitness(current_ind, edges_array)

    # Best solution ever
    best_ever = current_ind.copy()

    temp = initial_temp
    history = []

    for step in range(max_iters):
        # Generate neighbor using single gene mutation
        next_ind = current_ind.copy()
        single_gene_mutation(next_ind)
        next_fitness = evaluate_fitness(next_ind, edges_array)

        delta = next_fitness - current_fitness
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_ind = next_ind
            current_fitness = next_fitness

            if current_fitness < best_ever.fitness:
                best_ever = current_ind.copy()

        history.append(best_ever.fitness)

        temp *= cooling_rate
        if temp < 0.01:
            break

    return best_ever, history
        
