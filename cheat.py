
import random

def cheat_number(input_string:str)->int:
       while True:
        try:
            num = int(input(input_string))
            return num
        except ValueError:
            print('ALARM!')

def cheat_list(num:int)-> list:
    lst_num = [random.randint(0, 10) for _ in range(num)]
    return lst_num 

def cheat_point(input_string:str)->list:
   
    while True:
        try:
            a = input(input_string)
            lst = list(map(int, a.split(' ')))
            return lst
        except ValueError:
            print('ERROR 404')