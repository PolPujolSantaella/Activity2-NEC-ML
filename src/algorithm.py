import random
from src.chromosome import Individual
from src.fitness import evaluate_fitness

def run_genetic_algorithm(graph, pop_size, max_generations, max_colors,
                          selection_func, crossover_func, mutation_func,
                          mutation_rate, elitism_count=2):
    
    num_nodes = graph.number_of_nodes()

    # 1. Initialize population
    population = [Individual(num_nodes, max_colors) for _ in range(pop_size)]

    # 2. Evaluate fitness of initial population
    for ind in population:
        evaluate_fitness(ind, graph)

    best_ever = max(population, key=lambda ind: ind.fitness).copy()
    generations_no_improvement = 0
    history = []

    # 3. Main loop Evolutionary process
    for gen in range(max_generations):
        # Sort population by fitness (descending)
        population.sort(key=lambda x: x.fitness, reverse=True)

        # Store hystory
        current_best = population[0]
        history.append(current_best.fitness)

        # Actualize best ever individual
        if current_best.fitness > best_ever.fitness:
            best_ever = current_best.copy()
            generations_no_improvement = 0
        else:
            generations_no_improvement += 1

        # Stationart condition
        # If no improvement for 100 generations, stop
        if generations_no_improvement >= 100:
            print(f"Stationary condition met at generation {gen}.")
            break

        # New Population (Start with elites)
        new_population = [ind.copy() for ind in population[:elitism_count]]

        # Fill the rest of the new population
        while len(new_population) < pop_size:
            # Selection
            parent1 = selection_func(population)
            parent2 = selection_func(population)

            # Crossover
            child1_genes, child2_genes = crossover_func(parent1, parent2)

            # Create child individuals
            h1, h2 = Individual(num_nodes, max_colors), Individual(num_nodes, max_colors)
            h1.genes, h2.genes = child1_genes, child2_genes

            # Mutation
            mutation_func(h1, mutation_rate, max_colors)
            mutation_func(h2, mutation_rate, max_colors)

            # Evaluate fitness
            evaluate_fitness(h1, graph)
            evaluate_fitness(h2, graph)

            new_population.extend([h1, h2])

        population = new_population[:pop_size]


    return best_ever, history
