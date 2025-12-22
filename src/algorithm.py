import random
from src.chromosome import Individual
from src.fitness import evaluate_fitness

def run_genetic_algorithm(graph, pop_size, max_generations, max_colors,
                          selection_func, crossover_func, mutation_func,
                          mutation_rate, elitism_count=2):
    
    num_nodes = graph.number_of_nodes()

    # Initialize population
    population = [Individual(num_nodes, max_colors) for _ in range(pop_size)]

    # Evaluate fitness of initial population
    for ind in population:
        evaluate_fitness(ind, graph)
