text = 'Съешь ещё этих мягких французских булок, да выпей чаю'
print('Длина строки:', len(text))

result = text[-10:-2]  # c 2 символа с конца до 10 с конца не включая
print(result)

result = text[4:]  # с 4 символа до конца
print(result)

result = text[:10]  # с начала до 10 символа не включительно
print(result)

result = text[2:10]  # с 2 до 10 символа не включительно
print(result)
