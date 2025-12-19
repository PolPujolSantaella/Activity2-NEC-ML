import numpy as np

def evaluate_fitness(individual, graph):
    """
    Calculate fitness based on conflicts.
    """

    conflicts = 0
    for u, v in graph.edges():

        # If two nodes adjacent have the same gene. It's a conflict.
        if individual.genes[u - 1] == individual.genes[v - 1]:
            print(f"Conflict between node {u} and node {v}")
            conflicts += 1
        
    individual.conflicts = conflicts

    # Fitness Function: Maximize this value
    # If conflicts = 0, fitness is high
    num_colors_used = len(np.unique(individual.genes))
    if conflicts == 0:
        # High fitness 
        individual.fitness = 1000 + (1.0 / num_colors_used)
    else:
        # Lower fitness
        individual.fitness = 1.0 / (conflicts + 1)

    return individual.fitness