"""
    Created by Rituraj Ghosh on 23/06/2022
"""
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
for row in picture:
    for pixel in row:
        if (pixel==1):
            print('*', end='')
        else:
            print(' ', end='')
    print('') #    *
              #   ***
              #  *****
              # *******
              #    *
              #    *