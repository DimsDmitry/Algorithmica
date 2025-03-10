"""Множество - неупорядоченный изменяемый набор уникальных элементов,
может содержать только неизменяемые структуры данных"""
set1 = {'яблоко', 'банан', 'кефир'}
print(set1)

set2 = {'яблоко', 'кефир', 'банан'}
print(set1 == set2)

# таким образом создать пустое множество нельзя
set1 = {}
print(type(set1))  # словарь

# способ 1
set1 = set()

# способ 2
set2 = {1, 2, 3}

# способ 3 - итерируемый объект
test_set = set('Привет, мир!')
print(test_set)

test_set = set('хлеб булочка кефир молоко хлеб'.split())
print(test_set)

cities = {
    ('Москва', 20000000),
    ('Питер', 7000000),
    ('Казань', 1500000)
}
print(cities)

# проверка наличия элемента
digits = {1, 2, 5, 10}
print(33 in digits)  # False
print(2 in digits)  # True

# способ 4 - с помощью генератора
even_squares = {x ** 2 for x in range(10) if x % 2 == 0}
print(even_squares)

# frozenset - замороженное множество, неизменяемая структура данных
my_set = frozenset([1, 2, 3, 4, 5, 5, 5])
print(my_set)

# добавление элементов
nums = {1, 2, 3}
nums.add(10)
print(nums)

nums.update([5, 9, 10])  # несколько элементов можно добавить списком, строкой или др итерируемым объектом
nums.update('a b c')
print(nums)

# множества нельзя сложить, но можно объединить
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.union(set2)
print(set3)

# удаление элементов из множеств
s = {1, 2, 10, 15}
s.remove(2)  # если элемента нет, возникнет исключение
print(s)

# более безопасный вариант:
s.discard(3)
print(s)

# удалить случайный элемент:
s = {1, 2, 10, 15}
s.pop()
print(s)

s.clear()  # очистить множество
print('\n' + 100 * '#' + '\n')

'''операции над множествами'''
# объединение
set1 = {1, 2, 3}
set2 = {4, 5, 6}

set3 = set1 | set2  # либо union
print(set3)

# пересечение - выводятся только ОБЩИЕ для множеств элементы
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 3}

set3 = set1 & set2
print(set3)
# функция:
set1.intersection(set2)
print(set1)

# разность - элементы принадлежащие ТОЛЬКО первому множеству
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

set3 = set1 - set2
set3 = set1.difference(set2)  # та же функция!
print(set3)

# удаление совпадающих элементов:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
set1 -= set2
set1.difference_update(set2)  # смысл тот же что и в -=
print(set1)

# симметрическая разность множеств
a = {'молоко', 'кефир', 'чай', 'булочка'}
b = {'молоко', 'кефир', 'сок', 'вишня'}
res = a ^ b
res = a.symmetric_difference(b)  # тоже самое
print(res)

print('\n' + 100 * '#' + '\n')
# проверка наличия элементов во множествах
set1 = {1, 1, 2, 3, 4}
print(len(set1))  # 4

set2 = set()
set3 = {1, 2, 3, 4}

print(bool(set2))  # False - пустое множество
print(bool(set3))  # True

'''сравнение множеств - операторы == или !='''
set1 = {2, 3, 4, 5}
set2 = {2, 3, 5, 4}
print(set1 == set2)  # True
print(set1 != set2)  # False

# проверка принадлежности элемента:
print(2 in set1)  # True
print(10 not in set1)  # True

# проверка на подмножество
set1 = {2, 3, 4, 1}
set2 = {2, 3, 5, 4}

print(set1.issubset(set2))  # False
