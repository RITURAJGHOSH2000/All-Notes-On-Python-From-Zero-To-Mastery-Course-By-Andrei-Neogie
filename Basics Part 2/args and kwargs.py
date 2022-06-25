"""
    Created by Rituraj Ghosh on 25/06/2022
"""
# *args **kwargs
def super_func(name, *args, i='Hi', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args)+total
print(super_func('Andy', 1,2,3,4,5, num1=5, num2=10)) # 30

# Rule: parameters, *args, default parameters, **kwargs