import random
import matplotlib.pyplot as plt

"""
This program uses a genetic algorithm to solve the 0/1 Knapsack problem. 
In the Knapsack problem, you are given a set of items, each with a value and a weight, 
and a knapsack with a weight limit. The goal is to select a combination of items 
to maximize the total value without exceeding the weight limit. 
This genetic algorithm iteratively evolves a population of candidate solutions to find the best combination.

Knapsack Problem Parameters:
- weight_limit: The weight limit of the knapsack.
- item_list: A list of items, where each item is represented as (value, weight).

Genetic Algorithm Parameters:
- population_size: The size of the population.
- max_generations: The maximum number of generations to run.
- mutation_rate: The probability of mutation for each gene in the chromosome.
- chromosome_length: The number of genes in each chromosome.
"""

# Knapsack Problem Parameters
weight_limit = 56
item_list = [(17, 1), (78, 20), (56, 34), (2, 15), (34, 21), (3, 10)]  # (value, weight)

# Genetic Algorithm Parameters
population_size = 100
max_generations = 300
mutation_rate = 0.5
chromosome_length = len(item_list)


def initialize_population():
    # Initialize the population with random chromosomes
    population = []
    for _ in range(population_size):
        chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
        population.append(chromosome)
    return population


def calculate_fitness(chromosome):
    # Calculate the fitness of a chromosome based on its value and weight
    total_value = 0
    total_weight = 0
    for gene, item in zip(chromosome, item_list):
        if gene == 1:
            total_value += item[0]
            total_weight += item[1]
    if total_weight > weight_limit:
        return 0  # Violates weight constraint
    return total_value


def selection(population):
    # Select individuals from the population based on their fitness
    selected = []
    total_fitness = sum(calculate_fitness(chromosome) for chromosome in population)
    for _ in range(population_size):
        r = random.uniform(0, total_fitness)
        cumulative_fitness = 0
        for chromosome in population:
            cumulative_fitness += calculate_fitness(chromosome)
            if cumulative_fitness >= r:
                selected.append(chromosome)
                break
    return selected


def crossover(parent1, parent2):
    # Perform one-point crossover to create two children
    crossover_point = random.randint(1, chromosome_length - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def mutation(chromosome):
    # Apply mutation to a chromosome with a given probability
    mutated_chromosome = chromosome[:]
    for i in range(chromosome_length):
        if random.random() < mutation_rate:
            mutated_chromosome[i] = 1 - mutated_chromosome[i]
    return mutated_chromosome


def genetic_algorithm():
    # Main genetic algorithm loop
    population = initialize_population()
    fitness_history = []
    for generation in range(max_generations):
        population = selection(population)
        new_population = []
        while len(new_population) < population_size:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child1, child2 = crossover(parent1, parent2)
            mutated_child1 = mutation(child1)
            mutated_child2 = mutation(child2)
            new_population.extend([mutated_child1, mutated_child2])
        
        best_fit = max(calculate_fitness(chromosome) for chromosome in new_population)
        fitness_history.append(best_fit)
        
        population = new_population

    best_chromosome = max(population, key=calculate_fitness)
    best_fitness = calculate_fitness(best_chromosome)

    return best_chromosome, best_fitness, fitness_history


# Run the genetic algorithm and print the result
best_solution, best_fitness_value, fitness_history = genetic_algorithm()
print("Best Solution:", best_solution)
print("Best Fitness Value:", best_fitness_value)

# Plot fitness history
plt.plot(fitness_history)
plt.title('Fitness History')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.show()
