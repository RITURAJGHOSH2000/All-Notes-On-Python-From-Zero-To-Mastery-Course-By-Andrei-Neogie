"""
    Created by Rituraj Ghosh on 25/06/2022
"""
def checkDriverAge():
    age = input('Please enter your age: ')
    if int(age)<18:
        print('Sorry, you are too young to drive this car. Powering Off')
    elif int(age)==18:
        print('Congratulations on your first year of driving. Enjoy the ride!')
    elif int(age)>18:
        print('Powering on. Enjoy the ride!')
checkDriverAge()
# Please enter your age: 1
# Sorry, you are too young to drive this car. Powering Off

# Please enter your age: 18
# Congratulations on your first year of driving. Enjoy the ride! 

# Please enter your age: 60
# Powering on. Enjoy the ride!

def checkDriverAge(age):
    if int(age)<18:
        print('Sorry, you are too young to drive this car. Powering Off')
    elif int(age)==18:
        print('Congratulations on your first year of driving. Enjoy the ride!')
    elif int(age)>18:
        print('Powering on. Enjoy the ride!')
checkDriverAge(92)
# Powering on. Enjoy the ride!

def checkDriverAge(age = False):
    age = input('Please enter your age: ')
    if int(age)<18:
        print('Sorry, you are too young to drive this car. Powering Off')
    elif int(age)==18:
        print('Congratulations on your first year of driving. Enjoy the ride!')
    elif int(age)>18:
        print('Powering on. Enjoy the ride!')
checkDriverAge()
# Please enter your age: 18
# Congratulations on your first year of driving. Enjoy the ride!

# Please enter your age: 1
# Sorry, you are too young to drive this car. Powering Off

# Please enter your age: 60
# Powering on. Enjoy the ride!