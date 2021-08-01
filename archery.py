'''Riddler Nation is competing against Conundrum Country at an Olympic archery event. 
Each team fires three arrows toward a circular target 70 meters away. 
Hitting the bull’s-eye earns a team 10 points, while regions successively farther away 
from the bull’s-eye are worth fewer and fewer points.
Whichever team has more points after three rounds wins. 
However, if the teams are tied after each team has taken three shots, 
both sides will fire another three arrows. 
(If they remain tied, they will continue firing three arrows each until the tie is broken.)
For every shot, each archer of Riddler Nation has a one-third chance of hitting the 
bull’s-eye (i.e., earning 10 points), a one-third chance of earning 9 points and a 
one-third chance of earning 5 points.
Meanwhile, each archer of Conundrum Country earns 8 points with every arrow.
Which team is favored to win?
Extra credit: What is the probability that the team you identified as the favorite will win?'''

import numpy as np

conundrum_country_score = 24

def one_round():
    '''initalize score as 24.  if it's a tie, keep playing.  otherwise, return value'''
    round_score = 24
    while round_score == 24: ## if it's a tie, just keep simming until it isn't
        round_score = np.sum(np.random.choice([10, 9, 5], size = 3))
    return round_score

def play_some_games(n: int): ## specify number of sims
    sb = 0 ## scoreboard
    for x in range(n):
        riddler_nation = one_round()
        if riddler_nation > conundrum_country_score:
            sb += 1
        else:
            next
    return sb

n = 10**6 ## number of sims
rn_wins = play_some_games(n)

## display results
if rn_wins > rn_wins/2:
    print('winner:  **Riddler Nation**')
elif rn_wins < rn_wins/2:
    print('winner:  **Conundrum Country**')
else:
    print('It\'s a tie!')
print('wins:', str(rn_wins), '|', 'losses:', str(n - rn_wins))
print('winning percentage:', str(round(rn_wins/n * 100, 2)) + '%')
## Riddler Nation, 52.35% <-- my guess