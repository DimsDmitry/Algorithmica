test_list = [10, 16, 25, 0, 'Hello', 8, 4]

for num in test_list:
    try:
        print(10 / num)
    except TypeError:
        print('На строку делить нельзя!')  # или оператор continue
    except ZeroDivisionError:
        print('На ноль делить нельзя!')  # или оператор continue
