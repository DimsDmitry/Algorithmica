my_string = 'Hello world!'
result = my_string.index('e')
# если не находит элемент - возвращает ошибку
print(result)


# length - длина
text = 'ПРИВЕТ всем программистам!'
count_sym = len(text)  # возвращает int
print(count_sym)

# find - искать
text = text.lower()  # переводит все буквы в нижний регистр
print(text)
result = text.find('всем')  # возвращает int - индекс числа
# или если его нет - число -1
print(result)


text = text.upper()  # переводит все буквы в верхний регистр
print(text)

# оператор in
text = 'Я изучаю язык Python'.lower()
print('python' in text)

# replace - замена (переместить)