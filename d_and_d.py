import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def roll():
    roll = np.random.randint(low = 1, high = 21, size = 2)
    return roll

def roll_w_advantage():
    a = max(roll())
    return a

def roll_w_disadvantage():
    d = min(roll())
    return d

def roll_w_advantage_of_disadvantage():
    ad1 = min(roll())
    ad2 = min(roll())
    return max(ad1,ad2)

def roll_w_disadvantage_of_advantage():
    ad1 = max(roll())
    ad2 = max(roll())
    return min(ad1,ad2)

def single_roll():
    roll = np.random.randint(low = 1, high = 21, size = 1)
    return min(roll)

def show_histogram():
    plt.hist(single, bins = range(1,22), label = 'single roll', alpha = 0.7)
    plt.hist(aod, bins = range(1,22), label = 'ad of dis', alpha = 0.7)
    plt.hist(doa, bins = range(1,22), label = 'dis of ad', alpha = 0.7)
    plt.title('Histogram:  D&D roll methods')
    plt.xlabel('roll value')
    plt.ylabel('frequency')
    plt.xlim(1,21)
    plt.ylim(1,10000)
    plt.legend(loc='best')
    plt.xticks(range(1,21))
    plt.show()

sim_no = 100000
single = []
aod = []
doa = []
for x in range(sim_no):
    single.append(single_roll())
    aod.append(roll_w_advantage_of_disadvantage())
    doa.append(roll_w_disadvantage_of_advantage())

show_histogram()
print('Number of simulations:', format(sim_no,',d'))
print('Single roll:', round(sum(single)/len(single),2))
print('Advantage of disadvantage:', round(sum(aod)/len(aod),2))
print('Disadvantage of advantage:', round(sum(doa)/len(doa),2))

#Extra Credit

sim_no = 50000
probs_s = []
probs_a = []
probs_d = []

for n in range(1,21):
    count_s = 0
    count_a = 0
    count_d = 0
    for x in range(sim_no):
        sr = single_roll()
        ad = roll_w_advantage_of_disadvantage()
        da = roll_w_disadvantage_of_advantage()
        if sr >= n:
            count_s += 1
        if ad >= n:
            count_a += 1
        if da >= n:
            count_d += 1
    probs_s.append(count_s/sim_no)
    probs_a.append(count_a/sim_no)
    probs_d.append(count_d/sim_no)

plt.plot(np.arange(1,21,1),probs_s, label = 'single roll')
plt.plot(np.arange(1,21,1),probs_a, label = 'ad of dis')
plt.plot(np.arange(1,21,1),probs_d, label = 'dis of ad')
plt.xticks(range(1,21))
plt.title('Probability:  D&D roll methods')
plt.xlabel('roll value (>=)')
plt.ylabel('probability')
plt.legend(loc='best')
plt.show()

#Best strategy is to use disadvantage of advantage for rolls 1-13, then switch to
#single roll for 14-20.  Advantage of disadvantage is basically ineffective outside of
#rolling >= 1, which is guranteed for any method!