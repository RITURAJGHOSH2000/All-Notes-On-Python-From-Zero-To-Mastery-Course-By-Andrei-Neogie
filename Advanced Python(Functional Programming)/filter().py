my_list = [1, 2, 3]


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))
print(my_list)
# [1, 3]
# [1, 2, 3]

# Python’s filter() is a built-in function that allows you to process an iterable and extract those items that satisfy a given condition. This process is commonly known as a filtering operation. With filter(), you can apply a filtering function to an iterable and produce a new iterable with the items that satisfy the condition at hand. In Python, filter() is one of the tools you can use for functional programming.
