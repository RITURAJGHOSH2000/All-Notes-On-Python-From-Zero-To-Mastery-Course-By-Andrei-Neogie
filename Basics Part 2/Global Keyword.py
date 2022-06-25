"""
    Created by Rituraj Ghosh on 25/06/2022
"""
total = 0
def count():
    global total
    total += 1
    return total
count()
count()
print(count()) # 3
# The keyword 'global' helps to access the value of any variable present globally outside any function inside a function

# Another way to do this
total = 0
def count(total):
    total += 1
    return total
print(count(count(count(total)))) # 3