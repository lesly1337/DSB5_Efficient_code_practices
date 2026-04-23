#!/usr/bin/env python3

import sys
import resource

def read_file(file_name):
    with open("ml-25m/" + file_name, 'r') as file:
        for line in file:
            yield line.strip()

if __name__ == '__main__':
    start_usage = resource.getrusage(resource.RUSAGE_SELF)
    file_name = sys.argv[1]
    list_of_data = read_file(file_name)
    for line in list_of_data:
        pass
    end_usage = resource.getrusage(resource.RUSAGE_SELF)
    user_time = end_usage.ru_utime - start_usage.ru_utime
    system_time = end_usage.ru_stime - start_usage.ru_stime    
    memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024*1024*1024)
    print("Peak Memory Usage = " + f"{memory_usage:.3f} GB")
    print("User Mode Time + System Mode Time = " + f"{user_time+system_time:.2f}s")
