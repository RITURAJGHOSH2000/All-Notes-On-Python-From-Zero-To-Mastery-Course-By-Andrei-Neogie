"""
    Created by Rituraj Ghosh on 22/06/2022
"""
is_old = bool('hello')
is_licenced = bool(5)
print(bool('hello')) # True
print(bool(5)) # True           These outputs are set to true automatically by python

print(bool('')) # False
print(bool(0)) # False

#All values are considered "truthy" except for the following, which are "falsy":

# None
# False
# Zeros, including:
# 0
# 0.0
# 0j
# decimal.Decimal(0)
# fraction.Fraction(0, 1)
# Empty sequences and collections, including:
# [] - an empty list
# {} - an empty dict
# () - an empty tuple
# '' - an empty str
# b'' - an empty bytes
# set() - an empty set
# an empty range, like range(0)
# objects for which
# obj.__bool__() returns False
# obj.__len__() returns 0
# A "truthy" value will satisfy the check performed by if or while statements. We use "truthy" and "falsy" to differentiate from the bool values True and False.