import numpy as np

def evaluate_fitness(individual, graph_edges, conflict_weight=1000):
    """
    Calculate fitness based on conflicts.
    """
    
    # Get colors for all 'u' nodes and 'v' nodes simultaneously
    u_colors = individual.genes[graph_edges[:, 0]]
    v_colors = individual.genes[graph_edges[:, 1]]
    conflicts = np.sum(u_colors == v_colors)    

    individual.conflicts = conflicts

    # Fitness (minimization)
    # Fitness = (conflict_weight * number_of_conflicts) + number_of_colors_used
    
    num_colors_used = len(np.unique(individual.genes))
    individual.fitness = conflict_weight * conflicts + num_colors_used

    return individual.fitness