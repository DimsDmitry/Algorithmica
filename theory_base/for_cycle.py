# start = 2
# stop = 15
# step = 3
#
# for i in range(start, stop, step):
#     print(i)


string = 'Я гулял на море, мимо проплывали корабли, солнце садилось'

count_a = 0
for symbol in string:
    if symbol == 'а':
        count_a += 1
print('Букв а в строке:', count_a)