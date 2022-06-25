"""
    Created by Rituraj Ghosh on 25/06/2022
"""
# Scope is what variables do i have access to
a=1
def confusion():
    a=5
    return a
print(confusion())
print(a) 
# 5
# 1
# This is because at first a is assigned with 1 and then confusion function is stored somewhere in memory, when we print that function then within that function the value of a is 5 and ones it is executed then after that when we print the value of a which is still 1 globally and had not changed to 5 because the value of a = 5 was only inside the function confusion

# Rules of scope
# 1 - start with local
# 2 - then look for in the parent local scope
# 3 - global, here a=1 is the global
# 4 - built in python functions