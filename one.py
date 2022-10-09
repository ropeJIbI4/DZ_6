import cheat as c

print('!!!Программа определяет, присутствует ли в заданном списке строк, некоторое число!!!')
elem_lst = [input('Введите элемент списка:') for _ in range (c.cheat_number('Введите размер списка: '))]
num = c.cheat_number('Введите число: ')
result = list(filter(lambda x: x == str(num), elem_lst))
if result == []:
    print(f'Числа {num} нет ')
else:
    print(f'Число {num} есть ')
