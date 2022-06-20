"""
    Created by Rituraj Ghosh on 20/06/2022
"""
# List slicing
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
print(amazon_cart[0::1]) # ['notebooks', 'sunglasses', 'toys', 'grapes']
# Here also like string we can slice the list as needed

amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
amazon_cart[0] = 'laptop'
print(amazon_cart) # ['laptop', 'sunglasses', 'toys', 'grapes']
# lists are mutable i.e., a part of the list can be changed whenever required unlike strings which are immutable