import cheat as c

print('!!!Программа определит, позицию второго вхождения строки в списке либо сообщить, что её нет!!!')
elem_lst = [input('Введите элемент списка:') for _ in range (c.cheat_number('Введите размер списка: '))]
elem = input('Введите элемент для поиска: ')
result = [i for j, i in zip(elem_lst, list(range(len(elem_lst)))) if  j == elem]
if len(result) > 1:
    print(result[1])
else:
    print('Нет вхождения')