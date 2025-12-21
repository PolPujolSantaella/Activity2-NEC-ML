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


def roulette_wheel_selection(population):
    """
    Probability of select an individual is proportional to its fitness.
    """


#######################
# CROSSOVER OPERATORS
#######################

def single_point_crossover(parent1, parent2):
    """
    Perform single-point crossover between two parents.
    """

def uniform_crossover(parent1, parent2):
    """
    Perform uniform crossover between two parents.
    """

#######################
# MUTUATION OPERATORS
#######################

def random_resetting(individual, mutation_rate=0.01, max_colors=10):
    """
    Randomly reset genes in the individual with a given mutation rate.
    """

def swap_mutation(individual, mutation_rate=0.01):
    """
    Swap two genes in the individual with a given mutation rate.
    """
