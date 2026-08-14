from tool import Tools
from player import Player
from block import Block
import sys

def main():
    block = None
    player = None
    tool = None
    while True:
        try:
            options = int(input(("Welcome to text based game\n 1. Select Parameters\n 2. Play Game\n 3. Exit\n Selection: ")))
            match(options):
                case(1):
                    block, player, tool = option1()
                case (2):
                    if block is None:
                        block, player, tool = option1()
                    option2(block, player, tool)
                case (3):
                    break
        except ValueError:
            print("Enter Valid Input")
            continue


def option1():
    while True:
        try:
            playername = input("Player Name: ") 
            blockname = input("Block Name: ")
            max = int(input("Block X and Y (Both same as squares): "))
            resource = int(input("Resource Gained From Block: "))
            durabilitytaken = int(input("Durability taken of tool per hit: "))
            toolname = input("Tools: wooden pickaxe, stone pickaxe, iron pickaxe, diamond pickaxe, netherite Pickaxe: ").strip().lower()
            if toolname not in ["wooden pickaxe,stone pickaxe,iron pickaxe,diamond pickaxe,netherite pickaxe"]:
                toolname = input("Tools: wooden pickaxe, stone pickaxe, iron pickaxe, diamond pickaxe, netherite Pickaxe: ").strip().lower()

            block = Block(max, resource, durabilitytaken, blockname)
            player = Player(playername)
            tool = Tools(toolname)
            option = int(input("Options:\n 1. Reset set parameters\n 0. Main Menu: "))
            if option == 1:
                continue
            else:
                return [block, player, tool]
        except ValueError:
            continue


def option2(block, player, tool):
    round = 0
    options = int(input((f'Parameters set:\n 1. {player}\n 2. {block}\n 3. {tool}\n Press 1 to continue or 0 to exit main menu: ')))
    if options == 1:
        pass
    else:
        return
    while tool.durability > 0:
        try:
            mine = input("Type 'mine' to mine or exit to go back to main menu: ").lower().strip()
            if mine == "mine":
                block.renderblock()
                block.damage(tool.damage)
                tool.tooldamage(block.durabilitytaken)
                if block.blockbroken():
                    print("Block Broken")
                    player.gain(block.resource)
                    print(f'Player Inventory: {player.playerinventory}')
                    block.regenerate()
                    round += 1
            elif mine == "exit":
                options = int(input((f'Parameters set:\n 1. {player}\n 2. {block}\n 3. {tool}\n Press 1 to continue or 0 to exit main menu: ')))
                if options == 1:
                    continue
                else:
                    return
        except ValueError:
            continue

if __name__ == "__main__":
    main()