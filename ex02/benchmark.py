#!/usr/bin/env python3
import timeit
import sys

def check_gmail(mail):
    mail_index = mail.index("@")
    return mail[(mail_index + 1):(mail_index + 6)] == "gmail"
def loop(list_):
    result_list = []
    for mail in list_:
        if (check_gmail(mail)):
            result_list.append(mail)
    return result_list

def list_comp(list_):
    return [ mail for mail in list_ if check_gmail(mail)]

def map_f(list_):
    return map(lambda mail: mail, filter(lambda mail: check_gmail(mail), list_))

def filter_(list_):
    return filter(check_gmail, list_)    
if __name__ == '__main__':

    if ( len(sys.argv) == 3 ):
        func_name = sys.argv[1]
        num_of_operations = int(sys.argv[2])

        emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"]
        dupl_emails = [*emails, *emails, *emails, *emails, *emails]

        func_time = 0
        match func_name:
            case "loop":
                func_time = timeit.timeit('loop(dupl_emails)', setup="from __main__ import loop, dupl_emails", number=num_of_operations)
                # print("LOOP LIST: " + str(loop(dupl_emails))) 
            case "list_comprehension":
                func_time = timeit.timeit('list_comp(dupl_emails)', setup="from __main__ import list_comp, dupl_emails", number=num_of_operations)
                # print("LIST COMPREHENSION LIST: " + str(list_comp(dupl_emails))) 
            case "map":
                func_time = timeit.timeit('map_f(dupl_emails)', setup="from __main__ import map_f, dupl_emails", number=num_of_operations)   
                # print("MAP LIST: " + str(list(map_f(dupl_emails))))    
            case "filter":
                func_time = timeit.timeit('filter_(dupl_emails)', setup="from __main__ import filter_, dupl_emails", number=num_of_operations) 
                # print("FILTER LIST: " + str(list( filter_(dupl_emails))))    
            case _:
                raise ValueError("Wrong function name typed")  
        print(func_time)

