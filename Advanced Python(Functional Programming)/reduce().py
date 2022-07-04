from functools import reduce
my_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))
print(my_list)
# 0 1
# 1 2
# 3 3
# 6
# [1, 2, 3]

# Python’s reduce() is a function that implements a mathematical technique called folding or reduction. reduce() is useful when you need to apply a function to an iterable and reduce it to a single cumulative value. Python’s reduce() is popular among developers with a functional programming background, but Python has more to offer.
