# list1 = [1, 2, 3, 4, 5, 'string', [10, 14, 16]]
# list2 = [22, 23, 24]
#
#
# list1.append(12)
# print(list1)
# list1.insert(2, 9)
# # нежелательно складывать списки с помощью + :
# print(list1+list2)
# # лучше использовать:
# list1.extend(list2)
# print(list1)
#
# list1 = [5, 7, 10]
# # удаление элемента по его индексу
# digit = list1.pop(2)
# # удаление элемента по его значению! удаляется первое значение
# list1.remove(5)
#
# list1 = [2, 5, 7, 2, 10, 15, 2]
# while 2 in list1:
#     list1.remove(2)
#     # удаление всех значений 2
# print(list1)
#
# # list1.clear() - полная очистка списка
# # срез

list2 = ['text', 'hello', 4, 2, 10, 15]
print(list2[:3]) # от 0 до 3
print(list2[3:]) # от 3 до конца
print(list2[1:5:2]) # от 1 до 5 с шагом 2


