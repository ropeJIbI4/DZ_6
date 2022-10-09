import cheat as c

print('!!!Программа находит сумму чисел списка стоящих на нечетной позиции!!!')
number = abs(c.cheat_number('Введите размер списка, это должно быть целое число: '))
lst = c.cheat_list(number)
result = sum([i for j, i in enumerate(lst) if j % 2])
print('Список элементов:\n', lst)
print('Сумма на нечетных позициях =', result)
