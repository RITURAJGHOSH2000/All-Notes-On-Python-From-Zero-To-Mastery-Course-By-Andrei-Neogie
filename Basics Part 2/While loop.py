"""
    Created by Rituraj Ghosh on 23/06/2022
"""
i = 0
while i < 50:
    print(i) # This will print unlimited number of 0s as the value of i will remain 0 and will not change

i = 0
while i < 50:
    print(i)
    i += 1
else:
    print('Done with all the work') # Here 0 to 49 will be printed and then the last line will be printed

while True:
    input('say something: ')
    break # say something: Hi

while True:
    response = input('say something: ')
    if (response == 'bye'):
        break # say something: Hi
              # say something: hi
              # say something: bye