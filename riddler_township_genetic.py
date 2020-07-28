import numpy as np
import pandas as pd
import math

electoral_votes = [3,4,5,6,7,8,9,10,11,12]
shire_pops = [11,21,31,41,51,61,71,81,91,101]
popular_votes = [math.ceil(x/2) for x in shire_pops]
votes_to_win = math.ceil(sum(electoral_votes)/2)

def create_population(n):
    global df, pop, master_pop
    master_pop = []
    while len(master_pop) != n:
        check = list(np.random.binomial(1, 0.5, 10))
        if sum([y for x, y in zip(check,electoral_votes) if x != 0]) == votes_to_win:
            master_pop.append(check)
    df = pd.DataFrame(pd.Series(master_pop), columns=['votes'])
    df['score'] = cost_function(master_pop)
    df['rank'] = df['score'].rank(ascending=False)
    df['prob'] = pd.Series(df['rank'])/sum(pd.Series(df['rank']))

def cost_function(value):
    global scores
    scores = []
    for bb in range(len(value)):
        temp_score = 0
        temp_score = sum([y for x, y in zip(value[bb],popular_votes) if x != 0])
        scores.append(temp_score)
    return scores

def crossover(df, threshold, mutation_rate):
    global new_population, p_a, p_b, p_o
    parents = np.random.choice(df['votes'], size = 2, p = df['prob'], replace = False)
    slicers = np.random.randint(0,len(electoral_votes),2)
    thresh = np.random.uniform(0,1,1)
    if thresh <= 1:
        for x in slicers:
            p_a = parents[0][0:x]
            p_b = parents[1][x:]
            p_o = p_a + p_b
            mutation(0.03)
    if sum([y for x, y in zip(p_o,electoral_votes) if x != 0]) >= votes_to_win:
        new_population.append(p_o)

def mutation(rate):
    global p_o, p_o_list, max_score
    if np.random.choice([0,1], size = 1, p = [1 - rate, rate]) == 1:
        index = int(np.random.randint(0,len(p_o),1))
        if p_o[index] > 0:
            p_o[index] = int(np.random.choice([0,1], size = 1))

def breed(pop_size, mutation_rate):
    global df, new_population, max_score
    new_population = []
    while len(new_population) != pop_size:
        try:
            crossover(df,0.90,mutation_rate)
        except:
            create_population(pop_size)
            crossover(df,0.90,mutation_rate)
    df['votes'] = new_population
    df['score'] = cost_function(new_population)
    df['rank'] = df['score'].rank(ascending=False)
    df['prob'] = pd.Series(df['rank'])/sum(pd.Series(df['rank']))

create_population(100)
while len(pd.Series(df.score.unique())) != 1:
    breed(100,.03)

print(df['votes'].iloc[0])
print(df['score'].iloc[0])