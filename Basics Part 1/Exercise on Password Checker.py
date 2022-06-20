"""
    Created by Rituraj Ghosh on 19/06/2022
"""
# Create a password checker
user_name = input('Please enter your preferred username: ')
user_password = input('Please enter a strong password: ')
password = '*' * len(user_password)
print(f'Hey {user_name}, your password is {password} which is {len(user_password)} characters long')