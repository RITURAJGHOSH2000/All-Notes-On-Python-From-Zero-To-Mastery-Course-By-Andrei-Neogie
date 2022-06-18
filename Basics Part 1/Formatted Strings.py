"""
    Created by Rituraj Ghosh on 15/06/2022
"""
name = 'Joe'
age = 45
print(f'Hi {name}. Your age is {age}.') # Hi Joe. Your age is 45.
# Here 'f' represents formatted string which makes the print statement more cleaner and short, like this print statement can also be written without 'f' which will look like print('Hi ' + name + '. Your age is ' + str(age) + '.'), but it looks more complicated without formatted string. This type of formatted string concept is new in python 3 only, whereas python 2 had a different way for representing formatted string

print('Hi {}. Your age is {}'.format('Joe', '45')) # Hi Joe. Your age is 45. 
# This type of representing formatted string was used in python 2 

print('Hi {0}. Your age is {1}.'.format(name, age)) # Hi Joe. Your age is 45.
print('Hi {1}. Your age is {0}.'.format(name, age)) # Hi 45. Your age is Joe.
# As in computer science we start counting from 0, so here 0 is name and 1 is age as written in order after '.format'

print('Hi {new_name}. Your age is {age}.'.format(new_name = 'John', age = 50)) # Hi John. Your age is 50.
# As we changed the name and age at the print statement from Joe and 45 to John and 50 so we had to write the variables representing them in the {} which is written after '.format' at the respective positions in the string which is to be printed

# With '.format' things are little bit complicated, so it is recommended to write 'f' at the starting