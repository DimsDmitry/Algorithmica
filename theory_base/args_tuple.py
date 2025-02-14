# Функция с переменным количеством аргументов!

def multiply(*args):
    print(type(args))
    print(args)  # все аргументы помещаются в tuple - кортеж
    mul = 1
    for num in args:
        mul *= num
    return mul


result = multiply(5, 2, 4, 1, 10)
print(result)
