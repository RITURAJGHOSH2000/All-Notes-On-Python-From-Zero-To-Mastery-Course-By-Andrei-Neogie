"""
    Created by Rituraj Ghosh on 21/06/2022
"""
# Sets are unorderd collection of unique objects
my_set = {1,2,3,4,5,5}
print(my_set) # {1,2,3,4,5} ----> Here two 5s are not printed but only one is printed as in sets there are no duplicates , there has to be unique, so the last 5 is not added to the set
my_set.add(100)
my_set.add(2)
print(my_set) # {1,2,3,4,5,100} -----> Here as we can see that the 100 was added sucessfully but the 2 was not added as 2 is present in the set previously
print(set(my_set)) # {1,2,3,4,5,100}
print(1 in my_set) # True