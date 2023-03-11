a = input('Число a: ')
b = input('Число b: ')

try:
    a = int(a)
    b = int(b)
    c = a / b
    print(c)
except ValueError:
    print('Ошибка! a и b должны быть числом!')
except ZeroDivisionError:
    print('Ошибка! На ноль делить нельзя!')
finally:
    print('Этот кусок кода выполнится в любом случае!')

