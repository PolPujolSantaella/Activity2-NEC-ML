import random
import numpy as np

from src.chromosome import Individual
from src.fitness import evaluate_fitness

def run_genetic_algorithm(graph, pop_size, max_generations, max_colors,
                          selection_func, crossover_func, mutation_func,
                          mutation_rate=None, elitism_count=2, stationary_limit=200):
    
    num_nodes = graph.number_of_nodes()
    edges_array = np.array(graph.edges()) - 1

    # 1. Initialize population
    population = [Individual(num_nodes, max_colors) for _ in range(pop_size)]

    # 2. Evaluate fitness of initial population
    for ind in population:
        evaluate_fitness(ind, edges_array)

    best_ever = min(population, key=lambda ind: ind.fitness).copy()
    generations_no_improvement = 0
    history = []

    # 3. Main loop Evolutionary process
    for gen in range(max_generations):

        # 4. Sort population by fitness (ascending = best first))
        population.sort(key=lambda ind: ind.fitness)

        # Store hystory
        current_best = population[0]
        history.append(current_best.fitness)

        # Actualize best ever individual
        if current_best.fitness < best_ever.fitness:
            best_ever = current_best.copy()
            generations_no_improvement = 0
        else:
            generations_no_improvement += 1

        # Stationart condition
        # If no improvement for 100 generations, stop
        if generations_no_improvement >= stationary_limit:
            print(f"Stationary state reached at generation {gen}.")
            break

        # New Population
        new_population = []

        # 5. For pair in population size / 2
        while len(new_population) < pop_size - elitism_count:

            # 6. Selection
            parent1 = selection_func(population)
            parent2 = selection_func(population)

            # 7. Crossover
            child1, child2 = crossover_func(parent1, parent2)

            # 8. Mutation
            if mutation_rate is None:
                mutation_func(child1)
                mutation_func(child2)
            else:
                mutation_func(child1, edges_array, mutation_rate)
                mutation_func(child2, edges_array, mutation_rate)

            # 9. New Population
            new_population.extend([child1, child2])

        # 10. Elitism (add best individuals from previous population)
        elites = [population[i].copy() for i in range(elitism_count)]
        new_population.extend(elites)

        # 11. Replace population
        population = new_population[:pop_size]

        # 12. Evaluate fitness of new population
        for ind in population:
            evaluate_fitness(ind, edges_array)


    return best_ever, history
