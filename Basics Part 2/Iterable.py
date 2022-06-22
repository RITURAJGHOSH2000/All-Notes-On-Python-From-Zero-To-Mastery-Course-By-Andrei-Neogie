"""
    Created by Rituraj Ghosh on 22/06/2022
"""
# Iterable - list, dictionary, tuple, set, string
# Iterated -> one by one check each item in the collection
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}
for item in user.items():
    print(item) # ('name', 'Golem')
                # ('age', 5006)
                # ('can_swim', False)
for item in user.values():
    print(item) # Golem
                # 5006
                # False
for item in user.keys():
    print(item) # name
                # age
                # can_swim
for key, value in user.items():
    print(key, ':', value) # name : Golem
                           # age : 5006
                           # can_swim : False