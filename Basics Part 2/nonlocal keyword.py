"""
    Created by Rituraj Ghosh on 25/06/2022
"""
def outer():
    x="local"
    def inner():
        nonlocal x
        x="nonlocal"
        print("inner: ",x)
    inner()
    print("outer: ",x)
outer()
# inner:  nonlocal
# outer:  nonlocal

# Here the nonlocal keyword tell python that we don't want to assign a new value to the variable x but to call the already defined x from the parent local or the global one and the parent or the global variable will be changed to the newly assigned one