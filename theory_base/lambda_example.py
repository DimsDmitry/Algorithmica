from typing import List

def filter_even_numbers(numbers: List[int]) -> List[int]:
    return list(filter(lambda x: x % 2 == 0, numbers))

# Пример использования
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(numbers)
print(even_numbers)  # Вывод: [2, 4, 6, 8, 10]