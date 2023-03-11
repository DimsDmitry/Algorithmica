def is_palindrom(num):
    raw = str(num)
    r_num = int(raw[::-1])
    if num == r_num:
        return True
    return False

polindrom = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrom(i * j):
            polindrom.append(i * j)
print(max(polindrom))
