"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]


def is_prime(num):
    """
        simple_num = []
        for i in num:
            if i > 1:
                for d in range(2, i//2+1):
                    if i % d == 0:
                        break
                else:
                    if i not in simple_num:
                        simple_num.append(i)
        return simple_num
    """
    if num > 1:
        for d in range(2, num//2+1):
                if num % d == 0:
                    break
        else:
            return num

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(lambda num: num % 2 != 0, numbers))

    if filter_type == EVEN:
        return list(filter(lambda num: num % 2 == 0, numbers))

    if filter_type == PRIME:
        #return is_prime(numbers)
        return list(filter(is_prime, numbers))