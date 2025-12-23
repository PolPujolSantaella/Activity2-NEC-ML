import numpy as np
import random

#######################
# SELECTION OPERATORS
#######################

# Tournament Selection
def tournament_selection(population, k=3):
    """
    Select k individuals randomly and return the best one.
    """
    selected = random.sample(population, k)
    return max(selected, key=lambda ind: ind.fitness)


def roulette_wheel_selection(population):
    """
    Probability of select an individual is proportional to its fitness.
    """

    total_fitness = sum(ind.fitness for ind in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for individual in population:
        current += individual.fitness
        if current > pick:
            return individual
    return population[-1]

#######################
# CROSSOVER OPERATORS
#######################

def single_point_crossover(parent1, parent2):
    """
    Perform single-point crossover between two parents.
    """
    n = len(parent1.genes)
    point = random.randint(1, n - 1)

    child1_genes = np.concatenate((parent1.genes[:point], parent2.genes[point:]))
    child2_genes = np.concatenate((parent2.genes[:point], parent1.genes[point:]))

    return child1_genes, child2_genes

def uniform_crossover(parent1, parent2, p=0.5):
    """
    Perform uniform crossover between two parents.
    """

    n = len(parent1.genes)
    mask = np.random.rand(n) < p

    child1_genes = np.where(mask, parent1.genes, parent2.genes)
    child2_genes = np.where(mask, parent2.genes, parent1.genes)

    return child1_genes, child2_genes

#######################
# MUTUATION OPERATORS
#######################

def random_resetting(individual, mutation_rate=0.01, max_colors=10):
    """
    Randomly reset genes in the individual with a given mutation rate.
    """
    for i in range(len(individual.genes)):
        if random.random() < mutation_rate:
            individual.genes[i] = random.randint(0, max_colors - 1)

def swap_mutation(individual, mutation_rate=0.01, max_colors = 10):
    """
    Swap two genes in the individual with a given mutation rate.
    """
    if random.random() < mutation_rate:
        n = len(individual.genes)
        idx1, idx2 = random.sample(range(len(individual.genes)), 2)
        individual.genes[idx1], individual.genes[idx2] = individual.genes[idx2], individual.genes[idx1]
