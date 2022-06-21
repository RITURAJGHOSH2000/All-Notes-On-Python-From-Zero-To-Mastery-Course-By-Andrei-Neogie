"""
    Created by Rituraj Ghosh on 21/06/2022
"""
# Tuples are like lists but unlike lists they cannot be modified, they are immutable, they are more faster than list
from traceback import print_tb


my_tuple = (1,2,3,4,5)
# my_tuple[1] = 'z' ---> while we execute this line then it will display an error as we cannot modify tuples 
print(my_tuple[1]) # 2
print(5 in my_tuple) # True
# Tuples can be used as a key in the dictionary

# Python has two built-in methods that you can use on tuples
# count() - returns the number of times a specified value occurs in a tuple
# index() - searches the tuple for a specified value and returns the position of where it was found

print(my_tuple.count(5)) # 1
print(my_tuple.index(5)) # 4
print(len(my_tuple)) # 5