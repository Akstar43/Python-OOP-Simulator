from block import Block
from tool import Tools
from player import Player

def main():
    name = "iron"
    max = 10
    resource = 4
    durabilitytaken = 10
    block = Block(max, resource, durabilitytaken, name)
    playername = "Ak"
    player = Player(playername)
    tool = Tools("stone pickaxe")
    round = 0
    while tool.durability > 0:
        block.renderblock()
        block.damage(tool.damage)
        tool.tooldamage(block.durabilitytaken)
        if block.blockbroken():
            print("Block Broken")
            player.gain(block.resource)
            print(f'Player Inventory: {player.playerinventory}')
            block.regenerate()
            round += 1
    print(f'{player.name} has destroyed {block.name} - Rounds: {round} and inventory {player.playerinventory} using {tool}')
    print("Finish")

if __name__ == "__main__":
    main()
        
