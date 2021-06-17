def add(number, callback):
    """Производит арифметические действия с числами.
    Принимает число и функцию, выполняющую арифметическое действие.
    """    
    return callback(number)

def adder20(number):
    """Добавляет к аргументу 20."""
    return number + 20

def multiplier2(number):
    """Умножает аргумент на 2."""
    return number * 2

callback = 50
print(add(30, callback))