#!/usr/bin/env python3

import timeit
import sys
from functools import reduce

def loop(num):
    sum = 0
    for i in range(1, num+1):
        if i <= num:
            sum += i*i
    return sum
def reduce_(num):
    return reduce(lambda x,y: x + y*y, range(1, num+1))
if __name__ == '__main__':
    if ( len(sys.argv) == 4 ):
        func_name = sys.argv[1]
        num_of_operations = int(sys.argv[2])
        num = int(sys.argv[3])
        func_time = 0
        # print("Loop: " + str(loop(num)))
        # print("Reduce: " + str(reduce_(num)))
        match func_name:
            case "loop":
                func_time = timeit.timeit('loop(num)', setup="from __main__ import loop, num", number=num_of_operations)
            case "reduce":
                func_time = timeit.timeit('reduce_(num)', setup="from __main__ import reduce_, num", number=num_of_operations)
        print(func_time)
