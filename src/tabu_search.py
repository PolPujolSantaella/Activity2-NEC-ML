import numpy as np
from collections import deque

from src.chromosome import Individual
from src.fitness import evaluate_fitness
from src.genetic_operators import single_gene_mutation

def tabu_search(graph, max_colors, tabu_size=20, max_iters=1000, neighbor_size=10):
    """
    Tabu Search for graph coloring problem
    """

    num_nodes = graph.number_of_nodes()
    edges_array = np.array (graph.edges()) - 1 

    # Initialize first solution
    current_solution = Individual(num_nodes, max_colors)
    current_fitness = evaluate_fitness(current_solution, edges_array)

    best_ever = current_solution.copy()

    # Tabu List: Store the modified genes (node, previous color)
    tabu_list = deque(maxlen=tabu_size)

    history = [current_fitness]

    # Main loop
    for _ in range(max_iters):

        neighbors = []

        # Generate a set of candidates
        for _ in range(neighbor_size):
            candidate = current_solution.copy()
            single_gene_mutation(candidate)
            candidate_fitness = evaluate_fitness(candidate, edges_array)
            neighbors.append((candidate, candidate_fitness))

        # Sort neighbors (best fitness first)
        neighbors.sort(key=lambda x: x[1])

        # Select the best neighbor that is not tabú
        found_next = False
        for candidate, c_fitness in neighbors:
            # Convert genes to a tuple to compare with tabu list
            genes_tuple = tuple(candidate.genes)

            if genes_tuple not in tabu_list:
                # Accept although it's worse than the actual
                current_solution = candidate
                current_fitness = c_fitness
                tabu_list.append(genes_tuple)
                found_next = True
                break

        # If the neighbor is better than the best ever solution, accept
        if neighbors[0][1] < best_ever.fitness:
            current_solution = neighbors[0][0]
            current_fitness = neighbors[0][1]
            best_ever = current_solution.copy()
        elif found_next and current_fitness < best_ever.fitness:
            best_ever = current_solution.copy()

        history.append(best_ever.fitness)

    return best_ever, history