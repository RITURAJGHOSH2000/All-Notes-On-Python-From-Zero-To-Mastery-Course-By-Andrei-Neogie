"""
    Created by Rituraj Ghosh on 16/06/2022
"""
selfish = 'me me me'
        #  01234567
print(selfish[0]) # m
# Here in the print statement we want to print only the index of 0th position in the string present in the variable selfish, so to do that we use '[]' inside which we write the position number the index of which we want print
print(selfish[7]) # e
# In python the first item which we keep inside the [] is what we call as the starting point, here we can do an extra thing which is adding a ':' after start and giving the destination where to stop
print(selfish[0:5]) # me me
print(selfish[0:4]) # me m
# Another thing can be done i.e. after writing the destination location we can add another ':' and write how many steps to jump
print(selfish[0:8:3]) # mmm
print(selfish[1:]) # e me me  -> As here we have set the starting point but after : we didn't give any destination where to stop so it assumed that the coder wants to print the entire thing from the starting point; we can do the vise-versa also where we will not mention the starting point but will give the destination point and there it will assume that the coder wants to start printing from the 0th position to the mentioned destination point
print(selfish[:5]) # me me
print(selfish[::]) # me me me  -> Here as we did'nt mention any starting point, destination point and stepover values so all were set as default which means that there is no difference between the statement print(selfish) and the one we just executed
print(selfish[-1]) # e  -> In python the negetive index means start from the end of the string
print(selfish[-2]) # m
print(selfish[::-1]) # em em em  -> Here as we are giving the stepover value in negative so the execution starts from reverse
print(selfish[::-2]) # e me 