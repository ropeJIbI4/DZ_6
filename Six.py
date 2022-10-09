import cheat as c

print('!!!Программа формирует список из N членов последовательности!!!')
num = abs(c.cheat_number('Введите число для создания последовательности: '))
lst_num = list((-3) ** i for i in range(num))
print(lst_num)