from block import Block
from tool import Tools
from player import Player
def main():
    name = "iron"
    max = 10
    resource = 4
    durabilitytaken = 10
    block = Block(max, resource, durabilitytaken, name)
    player = Player()
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
    print("Finish")
    print(tool)
    print(f'Blocks destroyed {block.name} - Rounds: {round}')

if __name__ == "__main__":
    main()
        
