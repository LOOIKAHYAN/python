 
import time
def gettime(n):
    start = time.time()
    sum = 0
    for i in range(n):
        sum = sum + i

    end = time.time()

    timetake = end - start
    return timetake

print(gettime(999090))