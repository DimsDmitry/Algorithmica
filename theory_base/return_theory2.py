def do_something(a, b, c):
    return a*b*c, a+b+c

# оператор return ЗАВЕРШАЕТ РАБОТУ ФУНКЦИИ
# и ВОЗВРАЩАЕТ из неё значение!

result1, result2 = do_something(10, 2, 2)
# функция вернёт кортеж из двух чисел!!
# можно РАСПАКОВАТЬ ЕГО в разные переменные
print(result1)
print(result2)

def do_something(a, b, c):
    do = input('Умножаем или складываем? (1/2)')
    if do == '1':
        return a * b * c
    return a + b + c


# блок else не нужен, потому что если не выполнится
# do == '1', то автоматически выполнится строка 5

result = do_something(10, 2, 2)
# функция вернёт либо сумму, либо произведение
print(result)

