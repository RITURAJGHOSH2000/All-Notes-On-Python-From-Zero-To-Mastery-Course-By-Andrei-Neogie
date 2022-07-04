from functools import reduce
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize(string):
    return string.upper()


print(list(map(capitalize, my_pets)))  # ['SISI', 'BIBI', 'TITI', 'CARLA']
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
s = sorted(my_numbers)
# or we can sort directly in the print statement like print(list(zip(my_strings, sorted(my_numbers))))
print(list(zip(my_strings, s)))
# [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
scores = [73, 20, 65, 19, 76, 100, 88]


def passed_student(score):
    return score > 50


print(list(filter(passed_student, scores)))  # [73, 65, 76, 100, 88]


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_numbers + scores))  # 456
