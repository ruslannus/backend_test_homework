from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(your_number):
    """Вычисляет квадратный корень."""
    return sqrt(your_number)


def calc(your_number):
    """Выводит на печать значение вычисления квадратного корня."""
    root = your_number
    if root = 0:
        print('на ноль делить нельзя')
    else:
        root = calculate_square_root(root)
    print(f'Мы вычислили корень квадратный из введенного вами числа. '
          f'Это будет: {root}')


print(message)
calc(13)