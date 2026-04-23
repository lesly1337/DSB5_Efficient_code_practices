import timeit

def check_gmail(mail):
    mail_index = mail.index("@")
    return mail[(mail_index + 1):(mail_index + 6)] == "gmail"
def loop(list):
    result_list = []
    for mail in list:
        if (check_gmail(mail)):
            result_list.append(mail)
    return result_list

def list_comp(list):
    return [ mail for mail in list if check_gmail(mail)]
if __name__ == '__main__':
    emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"]
    dupl_emails = [*emails, *emails, *emails, *emails, *emails]
    loop_time = timeit.timeit('loop(dupl_emails)', setup="from __main__ import loop, dupl_emails", number=90000000)
    list_comp_time = timeit.timeit('list_comp(dupl_emails)', setup="from __main__ import list_comp, dupl_emails", number=90000000)

    if ( loop_time > list_comp_time ):
        print("it is better to use a list comprehension")
        print(f"{list_comp_time} vs {loop_time}")
    elif (loop_time < list_comp_time):
        print("it is better to use a loop")
        print(f"{loop_time} vs {list_comp_time}")
    else:
        print("no difference")
        print(f"{loop_time} vs {list_comp_time}")

    #print("LOOP LIST: " + str(loop(dupl_emails)))    
    #print("LIST COMPREHENSION LIST: " + str(list_comp(dupl_emails)))    



'''
hannahco@su-c2 ex00 % python3 benchmark.py


it is better to use a list comprehension
4.509592913964298 vs 5.581669570994563

it is better to use a loop
4.96414024697151 vs 4.985642122977879

it is better to use a list comprehension
48.163492599036545 vs 48.41218628000934
'''
