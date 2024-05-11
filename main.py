print('Hi, PyCharm')
x = 43
y = 32
print(x * y)
print("End line")


def test():
    a = 1
    b = 2
    print(a, b)


test()


def test2(a, b, c):
    print(a, b, c)


test2(1, 2, 3)


def test(txt, *numbers, name='Kirill', **surnames):
    print(txt)
    print('Это числа: ' , numbers)
    print('Моё имя:', name)
    print('Ф-О', surnames)

test('Это функция!', 2, 3, 4, 5, Semen='Slepakov', Andrey='Vasnetsov')


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


print(factorial(996))
