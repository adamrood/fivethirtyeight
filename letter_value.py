import numpy as np

tens = ['TWENTY','THIRTY','FORTY','FIFTY','SIXTY','SEVENTY','EIGHTY','NINETY']
ones = ['ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
misc = ['HUNDRED', 'THOUSAND']

ten_list = [0,0]
one_list = [0]

for y in range(len(tens)):
    total = 0
    for x in tens[y]:
        total += (ord(x) - 64)
    ten_list.append(total)

for y in range(len(ones)):
    total = 0
    for x in ones[y]:
        total += (ord(x) - 64)
    one_list.append(total)

def get_val(number):
    global p1,p2,p3
    p1 = int(str(number)[0])
    p2 = int(str(number)[1])
    p3 = int(str(number)[2])

tups = []
for x in range(120,999):
    get_val(x)
    tups.append([x,(one_list[p1] + ten_list[p2] + one_list[p3] + 74)])

surv = []
for x in range(len(tups)):
    if tups[x][0] < tups[x][1]:
        surv.append(tups[x])

print(max(surv))