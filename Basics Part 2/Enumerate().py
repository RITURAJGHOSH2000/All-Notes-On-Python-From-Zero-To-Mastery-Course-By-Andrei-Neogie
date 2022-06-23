"""
    Created by Rituraj Ghosh on 23/06/2022
"""
for i,char in enumerate('Hellloooo'):
    print(i,char) # 0 H
                  # 1 e
                  # 2 l
                  # 3 l
                  # 4 l
                  # 5 o
                  # 6 o
                  # 7 o
                  # 8 o
# Here as we enumerate so the i is getting the index values and the char is getting the charecters printed i.e., we are getting access to the index values of each charecters

# Exercise
for i,number in enumerate(list(range(100))):
    if number == 50:
        print(i, number) # 50 50