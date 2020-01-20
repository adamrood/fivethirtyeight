import numpy as np
from collections import Counter
import pandas as pd

# trials = 10000000
# prob = 0.5

# four_games = np.random.binomial(4,prob,trials)

# print('The odds of going both 2-2 and 4-4: ' 
#     + str((Counter(four_games)[2]/trials)**2))


def moon():
    moonwalkers = np.random.choice(['walk','so'],1,p=[.4,.6])
    return moonwalkers

def dubs():
    doubloons = np.random.choice(['double','so'],1,p=[.2,.8])
    return doubloons

def taters():
    taters = np.random.choice(['hr','so'],1,p=[.1,.9])
    return taters


##moonwalkers

def moon_game(innings):
    global moon_score
    #moon_score = 0

    for x in range(innings):
        outs = 0
        walks = 0
        while outs < 3:
            val = moon()
            if val == 'so':
                outs += 1
            if val == 'walk':
                walks += 1
        if walks < 4:
            moon_score += 0
        if walks >= 4:
            moon_score += walks - 3

##doubloons

def dub_game(innings):
    global dub_score
    dub_score = 0

    for x in range(innings):
        outs = 0
        doubles = 0
        while outs < 3:
            val = dubs()
            if val == 'so':
                outs += 1
            if val == 'double':
                doubles += 1
        if doubles < 2:
            dub_score += 0
        if doubles >= 2:
            dub_score += doubles - 1

##taters

def tater_game(innings):
    global tater_score
    #tater_score = 0

    for x in range(innings):
        outs = 0
        hrs = 0
        while outs < 3:
            val = taters()
            if val == 'so':
                outs += 1
            if val == 'hr':
                hrs += 1
        tater_score += hrs

master_results = pd.DataFrame(columns=['Home','Away','Home_Score','Away_Score','Winner'])

##moon (home) vs. tater (away)
for x in range(50):
    tater_score = 0
    moon_score = 0
    tater_game(9)
    moon_game(8)
    if moon_score <= tater_score:
        moon_game(1)
    while moon_score == tater_score:
        tater_game(1)
        moon_game(1)
    winner = []
    if moon_score > tater_score:
        winner = 'Moonwalkers'
    else:
        winner = 'Taters'
    temp_df = pd.DataFrame(['Moonwalkers','Taters',moon_score,tater_score,winner]).T
    temp_df = temp_df.rename(columns={0: 'Home', 1: 'Away', 2: 'Home_Score', 3: 'Away_Score', 4: 'Winner'})
    master_results = master_results.append(temp_df)

##tater (home) vs. moon (away)
for x in range(50):
    tater_score = 0
    moon_score = 0
    tater_game(8)
    moon_game(9)
    if moon_score >= tater_score:
        tater_game(1)
    while moon_score == tater_score:
        moon_game(1)
        tater_game(1)
    winner = []
    if moon_score > tater_score:
        winner = 'Moonwalkers'
    else:
        winner = 'Taters'
    temp_df = pd.DataFrame(['Taters','Moonwalkers',tater_score,moon_score,winner]).T
    temp_df = temp_df.rename(columns={0: 'Home', 1: 'Away', 2: 'Home_Score', 3: 'Away_Score', 4: 'Winner'})
    master_results = master_results.append(temp_df)

print(master_results)