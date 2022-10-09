import cheat as c

print('!!!Программа найдет произведение пар чисел в списке (Парой считаем первый и последний элемент, второй и предпоследний и т.д.)!!!')
num = abs(c.cheat_number('Введите размер списка: '))
lst_num = c.cheat_list(num)
print('Ваш список:\n', lst_num)
len_num = len(lst_num) // 2 + len(lst_num) % 2
lst_1, lst_2 = lst_num[:len_num], lst_num[-1:len_num-2:-1]
lst_result = list(i*j for i, j in zip(lst_1, lst_2))
print('Результат произведения :\n', lst_result)