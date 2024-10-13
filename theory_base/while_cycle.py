password = '123'
answer = input('Пароль!')

while answer != password:
    print('Доступ запрещён!')
    answer = input('Пароль!')

print('Доступ получен')
