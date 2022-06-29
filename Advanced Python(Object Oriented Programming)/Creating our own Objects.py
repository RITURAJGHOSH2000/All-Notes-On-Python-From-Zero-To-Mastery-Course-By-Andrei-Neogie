"""
    Created by Rituraj Ghosh on 29/06/2022
"""


class PlayerCharacter:
    def __init__(self, name):
        self.name = name  # These are attributes or properties that objects have

    def run(self):
        print('run')


player1 = PlayerCharacter('Rituraj')
player2 = PlayerCharacter('Ron')
print(player1.name)  # Rituraj
print(player2.name)  # Ron
