my_list = [1, 3, 6, 8, 99, 12, 'строка', 16, 120, 1000]

for sym in my_list:
    try:
        print(sym/2, end=', ')
    except TypeError:
        continue
