
class Player:
    def __init__(self, name):
        self.playerinventory = 0
        self.name = name
    def __str__(self):
        return f'Player Name: {self.name}, Player Inventory: {self.playerinventory}'
    def gain(self, n):
        self.playerinventory += n 