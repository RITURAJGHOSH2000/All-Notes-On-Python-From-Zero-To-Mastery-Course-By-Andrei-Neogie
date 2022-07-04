my_list = [1, 2, 3]
your_list = [20, 30, 10]
print(list(zip(my_list, your_list)))
# [(1, 20), (2, 30), (3, 10)]

# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
