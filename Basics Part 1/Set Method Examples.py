"""
    Created by Rituraj Ghosh on 21/06/2022
"""
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set.difference(your_set)) # {1, 2, 3}
my_set.discard(5)
print(my_set) # {1, 2, 3, 4}
my_set.difference_update(your_set)
print(my_set) # {1, 2, 3}
print(my_set.intersection(your_set)) # {4, 5} -----> print(my_set & your_set) this also does the work of .intersection
print(my_set.isdisjoint(your_set)) # False
print(my_set.union(your_set)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  ----> print(my_set | your_set) this also does the work of .union
am_set = {4,5}
print(am_set.issubset(your_set)) # True
print(am_set.issuperset(your_set)) # False
print(your_set.issuperset(am_set)) # True