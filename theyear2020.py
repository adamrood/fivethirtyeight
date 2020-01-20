# To celebrate the new year, here’s a quick puzzle about the number 
# 2020. Of all the fractions out there that are greater than 1/2020 
# but less than 1/2019, one has the smallest denominator. 
# Which fraction is it?

import numpy as np
num = np.arange(2,20,1)
den = np.arange(2021,5000,1)

check = 0
for x in range(len(num)):
    for y in range(len(den)):
        check = num[x]/den[y]
        if check > (1/2020) and check < (1/2019):
            print('numerator: ' + str(num[x]))
            print('denominator: ' + str(den[y]))
            print(str(check) + ' is between ' + str(1/2020) + ' and ' + str(1/2019) + '.')
            break
    break