question = 'Купи слона!'
answer = input(question).lower()

while answer != 'куплю':
    answer = input(f'Все говорят {answer}, а ты купи слона!').lower()

print('Спасибо за покупку!')
