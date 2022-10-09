import cheat as c

print('!!!Программа находит расстояние между двумя точками пространства(числа вводятся через пробел)!!!')
point_a = c.cheat_point('Введите через пробел координаты точки :')
point_b = c.cheat_point('Введите через пробел координаты точки :')
result = round(sum([(j - i) ** 2 for i, j in zip(point_a, point_b)]) ** 0.5, 2)
print('Расстояние между точками =',{result})