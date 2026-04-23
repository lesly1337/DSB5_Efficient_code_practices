#!/usr/bin/env python3
import timeit
import random
from collections import Counter

def generate_list():
    return [random.randint(1, 100) for i in range(0, 1000000)]

def dict_num_count(list):
    result_dict = {}
    for i in range(0, len(list)):
        key = list[i]
        if ( key in result_dict ):
            result_dict[key] = result_dict[key] + 1
        else:
            result_dict[key] = 1
    return result_dict    

def top_ten_count(dictionary):
    sorted_dict = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    return sorted_dict[0:10]

def counter_(list):
    return Counter(list)

if __name__ == '__main__':
    test_list = generate_list()
    print("my function: " + str(timeit.timeit('dict_num_count(test_list)', setup="from __main__ import dict_num_count, test_list", number=1)))
    print("Counter: " + str(timeit.timeit('counter_(test_list)', setup="from __main__ import counter_, test_list", number=1)))
    my_dict = dict_num_count(test_list)
    counter_dict = counter_(test_list)
    # print(my_dict)
    # print(counter_dict)
    print("my top: " + str(timeit.timeit('top_ten_count(my_dict)', setup="from __main__ import top_ten_count, my_dict", number=1)))
    print("Counter's top: " + str(timeit.timeit('counter_dict.most_common()', setup="from __main__ import counter_dict", number=1)))