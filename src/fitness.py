import numpy as np

def evaluate_fitness(individual, graph):
    """
    Calculate fitness based on conflicts.
    """

    conflicts = 0
    for u, v in graph.edges():

        # If two nodes adjacent have the same gene. It's a conflict.
        if individual.genes[u - 1] == individual.genes[v - 1]:
            # print(f"Conflict between node {u} and node {v}")
            conflicts += 1
        
    individual.conflicts = conflicts

    # Fitness Function: Maximize this value
    # If conflicts = 0, fitness is high
    num_colors_used = len(np.unique(individual.genes))
    if conflicts == 0:
        # High fitness
        # There's no conflict, so reward based on number of colors used 
        individual.fitness = 1.0 + (1.0 / num_colors_used)
    else:
        # Lower fitness
        # The more the conflicts, the lower the fitness
        individual.fitness = 1.0 / (1 + conflicts)

    return individual.fitness