list1 = [1, 2, 3, 4, 5, 'string', [10, 14, 16]]
list2 = [22, 23, 24]

list1.append(12)
list1.insert(2, 9)
list1.extend(list2)
print(list1)

# list1 = [5, 7, 10]
# digit = list1.pop(2)
# list1.remove(2)

# list1 = [2, 5, 7, 2, 10, 15, 2]
# while 2 in list1:
#     list1.remove(2)
# print(list1)