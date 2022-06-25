"""
    Created by Rituraj Ghosh on 25/06/2022
"""
a='hihiihihihihihi'
if ((n:=len(a))>10):    # ':=' is the walrus operator
    print(f'too long {n} elements')
while ((n:=len(a))>1):
    print(n)
    a=a[:-1]
print(a)
# 15
# 14
# 13
# 12
# 11
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# h