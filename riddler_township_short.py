import itertools
import math

combos = list(itertools.product([0, 1], repeat = 10))

electoral_votes = [3,4,5,6,7,8,9,10,11,12]
shire_pops = [11,21,31,41,51,61,71,81,91,101]
votes_needed = [math.ceil(x/2) for x in shire_pops]

results = []
for bb in combos:
    if sum([y for x, y in zip(bb,electoral_votes) if x != 0]) >= 38:
        results.append([bb, sum([y for x, y in zip(bb,votes_needed) if x != 0]),
            sum([y for x, y in zip(bb,electoral_votes) if x != 0])])

print(min(results, key = lambda a: a[1]))
print(min(results, key = lambda a: a[1])[1]/sum(shire_pops))