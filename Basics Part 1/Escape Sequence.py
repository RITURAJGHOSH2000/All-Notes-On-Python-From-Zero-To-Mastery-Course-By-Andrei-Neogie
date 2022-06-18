"""
    Created by Rituraj Ghosh on 15/06/2022
"""
weather = "It's \"kind of\" sunny"
print(weather) # It's "kind of" sunny
# Here the '\' informs python that the things present after it, is a string which is known as escape sequence whereby using '\' we can uninterruptedly use the same "s or 's in a string 

weather = "It\\s \"kind of\" sunny"
print(weather) # It\s "kind of" sunny

weather = "\t It's \"kind of\" sunny \n \t Hope you have a great day!" # \t is tab where 't' after '\' tells python to add a tab space at that point of the string, \n is newline where 'n' after '\' tells python to start a new line from that point
print(weather) #    It's "kind of" sunny
               #    Hope you have a great day!