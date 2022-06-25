"""
    Created by Rituraj Ghosh on 25/06/2022
"""
# Write a code that will print the highest even number from the list 
def highest_even(li):
    evens = []
    for items in li:
        if items % 2 == 0:
            evens.append(items)
    return max(evens)
print(highest_even([10,2,3,4,8,11])) # 10