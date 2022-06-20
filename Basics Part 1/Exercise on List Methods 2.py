"""
    Created by Rituraj Ghosh on 20/06/2022
"""
# Fix this code so that it prints a sorted list of all of our friends (alphabetically). 
# friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
# new_friend = ['Stanley']
# print(friends.sort() + new_friend)

friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
friends.append('Stanley')
print(sorted(friends)) # ['Amira', 'Carrie', 'Chu', 'Joy', 'Patty', 'Simon', 'Stanley']

# Another way to do this is

friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
new_friend = ['Stanley']
friends.extend(new_friend)
print(sorted(friends)) # ['Amira', 'Carrie', 'Chu', 'Joy', 'Patty', 'Simon', 'Stanley']