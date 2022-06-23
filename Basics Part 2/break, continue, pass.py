"""
    Created by Rituraj Ghosh on 23/06/2022
"""
my_list = [1,2,3]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue # 1
             # 2
             # 3

# continue statement tells the interpreter to get back to the top of the enclosing loop 
# In the above program if we shift the print statement from line number 7 to the line after the continue statement then the print statement will not get executed and hence no output will occur
while i < len(my_list):
    print(my_list[i])
    i += 1
    pass # 1
         # 2
         # 3

# pass statement doesn't do anything as it simply tells python interpreter to pass to the next line