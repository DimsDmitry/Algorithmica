# def do_something(x, y):
#     """умножаем либо складываем"""
#     do = input('1 - сложить, 2 - умножить')
#     if do == '1':
#         print(x + y)
#     else:
#         print(x * y)
#
#
# do_something(5, 3)


def do_something(x, y):
    """умножаем либо складываем"""
    do = input('1 - сложить, 2 - умножить')
    if do == '1':
        return x + y
    return x * y


# ОПЕРАТОР return ЗАВЕРШАЕТ работу функции и ВОЗВРАЩАЕТ из неё значение

# result = do_something(5, 3)
# print(result)


def do_something2(x, y):
    """Функция может возвращать несколько значений!"""
    return x + y, x * y


result = do_something2(10, 3)
print(result)
print(type(result))
