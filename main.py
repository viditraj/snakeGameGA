from Genetic_Algorithm import *
from Snake_Game import *
from helper import plot
import numpy as np

# n_x -> no. of input units
# n_h -> no. of units in hidden layer 1
# n_h2 -> no. of units in hidden layer 2
# n_y -> no. of output units

# The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
sol_per_pop = 50
num_weights = n_x * n_h + n_h * n_h2 + n_h2 * n_y

# Defining the population size.
pop_size = (sol_per_pop, num_weights)
# Creating the initial population.
new_population = np.random.choice(np.arange(-1, 1, step=0.01), size=pop_size, replace=True)

num_generations = 1000
total_fitness = []
mean_fitness = []
best_fitness = -1
best_individual = None
num_parents_mating = 12
fittest_chromosome = None
best_chromosome = None
max_fitness = -1
i = 0
for generation in range(num_generations):
    print('##############        GENERATION ' + str(generation) + '  ###############')
    # Measuring the fitness of each chromosome in the population.
    fitness, fittest_chromosome = cal_pop_fitness(new_population)
    print('#######  fittest chromosome in gneneration ' + str(generation) + ' is having fitness value:  ',
          np.max(fitness))
    meanf = np.mean(fitness)
    mean_fitness.append(meanf)
    plot(fitness, mean_fitness, i)
    i +=1
    if max_fitness < np.max(fitness):
        max_fitness = np.max(fitness)
        best_chromosome = fittest_chromosome

    if np.max(fitness) > best_fitness:
        best_fitness = np.max(fitness)
        best_individual = new_population[np.argmax(fitness), :]

    # Selecting the best parents in the population for mating.
    parents = select_mating_pool(new_population, fitness, num_parents_mating)

    # Generating next generation using crossover.
    offspring_crossover = crossover(parents, offspring_size=(pop_size[0] - parents.shape[0], num_weights))

    # Adding some variations to the offsrping using mutation.
    offspring_mutation = mutation(offspring_crossover)

    # Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

np.save('best_individual.npy', best_chromosome)

best_individual = np.load('best_individual.npy')
score = run_game_with_ML(display, clock, best_individual)

print(score)
