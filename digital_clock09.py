# A digital 12-hour clock displays 10 digits: two digits representing the hour (from “00” to “12”), 
# two digits representing the minute, two digits representing the second and four digits representing the year.
# When will the clock next use every digit from 0 to 9?

import numpy as np

hour = [x.zfill(2) for x in np.arange(1, 12 + 1, 1).astype(str)]
minute = [x.zfill(2) for x in np.arange(0, 60 + 1, 1).astype(str)]
second = [x.zfill(2) for x in np.arange(0, 60 + 1, 1).astype(str)]
year = list(np.arange(2031, 9999 + 1, 1).astype(str))

for w in year:
    for x in hour:
        for y in minute:
            for z in second:
                if len(set(w + x + y + z)) == 10:
                    print('Answer:',x + ':' + y + ':' +  z, w)
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break