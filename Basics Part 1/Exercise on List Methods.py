"""
    Created by Rituraj Ghosh on 20/06/2022
"""
# Exercise: Remove the Banana from the list, remove Blueberries from the list, put Kiwi at the end of the list, add Apples at the beginning of the list, count how many Apples are there in the basket and empty the basket
basket = ['Banana', 'Apples', 'Oranges', 'Blueberries']
1.
basket.pop(0)
print(basket) # ['Apples', 'Oranges', 'Blueberries']
2.
basket.pop()
print(basket) # ['Banana', 'Apples', 'Oranges']
3.
basket.append('Kiwi')
print(basket) # ['Banana', 'Apples', 'Oranges', 'Blueberries', 'Kiwi']
4.
basket.insert(0, 'Apples')
print(basket) # ['Apples', 'Banana', 'Apples', 'Oranges', 'Blueberries']
5.
number_of_apples = basket.count('Apples')
print(number_of_apples) # 2
6.
basket.clear()
print(basket) # []