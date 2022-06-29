"""
    Created by Rituraj Ghosh on 29/06/2022
"""
# Exercise


class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Apollo', 2)
cat2 = Cat('Luna', 3)
cat3 = Cat('Lulu', 1)


def oldest(*args):
    return max(args)


print(f'The oldest cat is {oldest(cat1.age, cat2.age, cat3.age)} years old')
