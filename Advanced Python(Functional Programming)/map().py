my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, my_list)))
print(my_list)
# [2, 4, 6]
# [1, 2, 3]

# Python’s map() is a built-in function that allows you to process and transform all the items in an iterable without using an explicit for loop, a technique commonly known as mapping. map() is useful when you need to apply a transformation function to each item in an iterable and transform them into a new iterable. map() is one of the tools that support a functional programming style in Python.
