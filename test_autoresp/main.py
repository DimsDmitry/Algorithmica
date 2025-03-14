from schedule import print_schedule, print_price


answer = input('Здравствуйте! 1-расписание тренировок, 2-цены тренировок')
while answer != 'стоп':
    if answer == '1':
        print_schedule()
    elif answer == '2':
        print_price()
    answer = input('Здравствуйте! 1-расписание тренировок, 2-цены тренировок')

print('До свидания!')