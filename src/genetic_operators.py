import numpy as np
import random

#######################
# SELECTION OPERATORS
#######################

# Tournament Selection
def tournament_selection(population, k=3):
    """
    Selects the best individual from a random subset of the population
    Fitness is assumed to be minimized.
    """
    selected = random.sample(population, k)
    return min(selected, key=lambda ind: ind.fitness)

def roulette_wheel_selection(population):
    """
    Roulette Wheel selection adapted for minimization problems.
    Probability is inversely proportional to fitness.
    """

    fitness_values = np.array([ind.fitness for ind in population])
    inverted_fitness = 1.0 / (fitness_values + 1.0)

    probabilities = inverted_fitness / np.sum(inverted_fitness)

    return np.random.choice(population, p=probabilities)

#######################
# CROSSOVER OPERATORS
#######################

def one_point_crossover(parent1, parent2):
    """
    One-point crossover between two parents.
    """

    # Select random point
    size = len(parent1)
    point = random.randint(1, size - 1)

    # Create children genes
    child1_genes = np.concatenate((parent1.genes[:point], parent2.genes[point:]))
    child2_genes = np.concatenate((parent2.genes[:point], parent1.genes[point:]))

    # Create children individuals
    child1 = parent1.copy()
    child2 = parent2.copy()

    # Assign genes to children
    child1.genes = child1_genes
    child2.genes = child2_genes

    return child1, child2

def uniform_crossover(parent1, parent2, p=0.5):
    """
    Perform uniform crossover between two parents.
    """

    # Mask for gene selection
    size = len(parent1)
    mask = np.random.rand(size) < p
    
    # Create children genes
    child1_genes = np.where(mask, parent1.genes, parent2.genes)
    child2_genes = np.where(mask, parent2.genes, parent1.genes)

    # Create children individuals
    child1 = parent1.copy()
    child2 = parent2.copy()

    # Assign genes to children
    child1.genes = child1_genes
    child2.genes = child2_genes

    return child1, child2

#######################
# MUTUATION OPERATORS
#######################

def single_gene_mutation(individual):
    """
    Always mutates exactly one randomly selected gene.
    """

    # Select random index
    idx = random.randint(0, len(individual) - 1)

    # Assign new random color
    new_color = random.randint(0, individual.max_colors - 1)

    # Ensure new color is different
    while new_color == individual.genes[idx]:
        new_color = random.randint(0, individual.max_colors - 1)

    individual.genes[idx] = new_color # Mutate gene

    return individual


def independent_gene_mutation(individual, graph_edges, mutation_rate=0.01):
    """
    Mutate conflicted genes using NumPy-based conflict detection.
    """

    # Access genes
    genes = individual.genes

    # Vectorized conflict detection
    u = graph_edges[:, 0]
    v = graph_edges[:, 1]

    conflict_mask = genes[u] == genes[v] # Identify conflicts

    if not np.any(conflict_mask):
        return individual  # No conflicts, nothing to mutate

    # Get unique conflicted nodes
    conflicted_nodes = np.unique(
        np.concatenate((u[conflict_mask], v[conflict_mask]))
    )

    # Apply mutation probabilistically
    for i in conflicted_nodes:
        if random.random() < mutation_rate:
            new_color = random.randint(0, individual.max_colors - 1)
            while new_color == genes[i]:
                new_color = random.randint(0, individual.max_colors - 1)
            genes[i] = new_color

    return individual