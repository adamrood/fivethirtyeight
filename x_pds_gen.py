import numpy as np
from collections import Counter
import random

across = [135, 45, 64, 280, 70]
down = [3000, 3969, 640]

def create_population(n):
    global pop
    pop = []
    for x in range(n):
        pop.append(np.random.randint(1, 10, size = (5, 3)))
    return pop

def cost_function(x):
    count = 0
    count += int(len([i for i, j in zip(np.prod(x, axis = 1), across) if i == j]))
    count += int(len([i for i, j in zip(np.prod(x, axis = 0), down) if i == j]))
    return count

def crossover(pop, threshold, mutation_rate):
    new_pop = []
    parents = random.choices([p[0] for p in pop], 
        k = 2, weights = [p[2] for p in pop])
    slicers = np.random.randint(0, 15, 1)
    thresh = np.random.uniform(0, 1, 1)
    if thresh <= 1:
        for x in slicers:
            y = 0
            new_sol = np.array(np.concatenate((parents[0][0:x], parents[1][x:]), axis = None)).reshape(5,3)
            mutation(new_sol, mutation_rate)
            if cost_function(new_sol) >= cost_function(parents[y]):
                new_pop.append(new_sol)
            else:
                if thresh <= 0.5:
                    new_pop.append(parents[y])
                else:
                    new_pop.append(new_sol)
            y += 1
    return new_pop

def score_population(pop):
    global score, prob
    score = []
    prob = []
    for x in pop:
        score.append(cost_function(x))
    for x in score:
        prob.append(x/sum(score))
    pop = list(zip(pop, score, prob))
    return pop

def mutation(solution, rate):
    indices = []
    if np.random.choice([0,1], size = 1, p = [1 - rate, rate]) == 1:
        mutations = np.random.randint(1, 10, size = 1)
        for x in range(len(mutations)):
            solution[np.random.randint(0,5), np.random.randint(0,3)] = x
    return solution

pop_size = 2500
selection_prob = 0.90
mutation_rate = 0.10

pop = create_population(pop_size)
pop = score_population(pop)
generation = []
while len(generation) != pop_size:
    generation.append(crossover(pop, selection_prob, mutation_rate))
generation = [item for sublist in generation for item in sublist]
new_pop = score_population(generation)
print(Counter([p[1] for p in new_pop]))
generation_counter = 1
while max([n[1] for n in new_pop]) != 8:
    generation = []
    while len(generation) != pop_size:
        generation.append(crossover(new_pop,selection_prob, mutation_rate))
    generation = [item for sublist in generation for item in sublist]
    new_pop = score_population(generation)
    print(Counter([p[1] for p in new_pop]))
    generation_counter += 1

print('Solved in',generation_counter,'generations!')
print([x[0] for x in new_pop if x[1] == 8][0])
