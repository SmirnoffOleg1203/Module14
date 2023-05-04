def find_monetka(x, y, r):

  if x**2 + y**2 <= r**2:

    print('Монетка где-то рядом')

  else:

    print('Монетки в области нет')

print('Введите координаты монетки: ')

x = float(input('X = '))

y = float(input('Y = '))

r = float(input('Введите радиус: '))

find_monetka(x,y,r)
