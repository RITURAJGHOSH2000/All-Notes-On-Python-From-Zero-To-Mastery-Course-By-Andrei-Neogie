"""
    Created by Rituraj Ghosh on 21/06/2022
"""
#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
#2 Iterate and print all the keys in the above user
#3 Add a new weapon to your user
#4 Add a new key to include 'is_banned'. Set it to false
#5 Ban the user by setting the previous key to True
#6 Create a new user2 by copying the previous user and update the age value and username value

user = {
    'age' : 30,
    'username' : 'Rituraj',
    'weapons' : ['M416', 'AKM', 'AWM', 'Groza'],
    'is_active' : True,
    'clan' : 'India'
}
print(user.keys()) # dict_keys(['age', 'username', 'weapons', 'is_active', 'clan'])
user['weapons'].append('MK14')
print(user) # {'age': 30, 'username': 'Rituraj', 'weapons': ['M416', 'AKM', 'AWM', 'Groza', 'MK14'], 'is_active': True, 'clan': 'India'}
user.update({'is_banned' : False})
print(user) # {'age': 30, 'username': 'Rituraj', 'weapons': ['M416', 'AKM', 'AWM', 'Groza', 'MK14'], 'is_active': True, 'clan': 'India', 'is_banned': False}
user['is_banned'] = True
print(user) # {'age': 30, 'username': 'Rituraj', 'weapons': ['M416', 'AKM', 'AWM', 'Groza', 'MK14'], 'is_active': True, 'clan': 'India', 'is_banned': True}
user2 = user.copy()
user2.update({'age' : 40, 'username' : 'Roshan'})
print(user2) # {'age': 40, 'username': 'Roshan', 'weapons': ['M416', 'AKM', 'AWM', 'Groza', 'MK14'], 'is_active': True, 'clan': 'India', 'is_banned': True}