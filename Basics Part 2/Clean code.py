"""
    Created by Rituraj Ghosh on 25/06/2022
"""
from ast import Return


def is_even_or_odd():
    num = input('Enter a number to check whether it is odd or even: ')
    num1 = int(num)
    if num1 % 2 == 0:
        print('It is an even number')
    elif num1 % 2 != 0:
        print('It is an odd number')
is_even_or_odd()
# Enter a number to check whether it is odd or even: 1
# It is an odd number

# Cleaning the above code a little bit, like if we want to check only for even 
def is_even_or_odd():
    num = input('Enter a number to check whether it is odd or even: ')
    num1 = int(num)
    if num1 % 2 == 0:
        print('It is an even number')
    else:
        print('It is an odd number')
is_even_or_odd()
# Enter a number to check whether it is odd or even: 2
# It is an even number

# Let's clean it up more
def is_even_or_odd(num):
    if num % 2 == 0:
        return True
    return False
print(is_even_or_odd(3)) # False

# Another way
def is_even_or_odd(num):
    return num % 2 == 0
print(is_even_or_odd(20)) # True