def multiply(*args):
    mul = 1
    for num in args:
        mul *= num
    return mul


result = multiply(5, 2, 4, 1, 10)
print(result)