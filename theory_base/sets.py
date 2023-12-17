# test_set = set()
test_set = {1, 1, '1', 5, 10, 5, 15}
print(test_set)

test_set.add(-4)  # add element
test_set.update([4, 9, 6])  # add many elems
test_set.discard(100)  # if cant delete, dont return exception
test_set.pop()  # delete random element
print(test_set)

fr = frozenset('abcde')
print(fr)
