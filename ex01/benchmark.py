import timeit

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
if __name__ == '__main__':
    emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"]
    dupl_emails = [*emails, *emails, *emails, *emails, *emails]

    loop_time = timeit.timeit('loop(dupl_emails)', setup="from __main__ import loop, dupl_emails", number=90000000)
    list_comp_time = timeit.timeit('list_comp(dupl_emails)', setup="from __main__ import list_comp, dupl_emails", number=90000000)
    map_time = timeit.timeit('map_f(dupl_emails)', setup="from __main__ import map_f, dupl_emails", number=90000000)

    dict_func_time = {"loop" : loop_time, "list comprehension" : list_comp_time, "map" : map_time }
    sorted_dict = sorted(dict_func_time.items(), key=lambda item: item[1])

    print("it is better to use a " + sorted_dict[0][0])
    for i, pair in enumerate(sorted_dict):
        print(sorted_dict[i][1], end='')
        if ( i != len(sorted_dict) - 1 ):
            print(" vs ", end='')
    # print()
    # print("LOOP LIST: " + str(loop(dupl_emails)))    
    # print("LIST COMPREHENSION LIST: " + str(list_comp(dupl_emails)))    
    # print("MAP LIST: " + str(list(map_f(dupl_emails))))    

'''
map(..) - ленивый итератор, элементы вычисляются по мере необходимости

hannahco@oa-g5 ex01 % python3 benchmark.py
it is better to use a map
0.3144866831135005 vs 4.654017756925896 vs 4.740703726187348%     


list(map(...)) - материализованный список, все элементы вычисляются сразу

it is better to use a loop
4.705883641028777 vs 4.83084458601661 vs 6.689085139892995% 
'''