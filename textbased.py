from tool import Tools
from player import Player
from block import Block
from save import Save
import csv
import os
import argparse
def main():
    save = Save()
    block = None
    player = None
    tool = None
    while True:
        try:
            options = int(input(("Welcome to text based game\n 1. Select Parameters\n 2. Play Game\n 3.  View Pass Games\n 4. Exit\n Option: ")))
            match(options):
                case(1):
                    block, player, tool = selectparams(save)
                case (2):
                    if block is None:
                        block, player, tool = selectparams(save)
                    startgame(block, player, tool, save)
                case (3):
                    viewprevgames(save)
                case (4):
                    print("Thank you for playing")
                    break
        except ValueError:
            print("Enter Valid Input")
            continue


def selectparams(save):
    options = int(input("1. Load from save 0. Add new Parameters:"))
    if options == 1:
        file_path = "saveparameter.csv"
        if not os.path.exists(file_path):
            pass
        else:
            with open("saveparameter.csv","r") as File:
                reader = csv.reader(File)
                rows = list(reader)
                for item in rows:
                    print(f'Count: {item[0]}. Block Name: {item[1]}, Block Max: {item[2]}, Block Resource: {item[3]}, Block Durability Taken: {item[4]}, Player Name: {item[5]}, Toolname: {item[6]} ')
                choice = int(input("Enter Count chosen: "))
                for row in rows:
                    if choice == int(row[0]):
                        block = Block(int(row[2]), int(row[3]), int(row[4]), row[1])
                        player = Player(row[5])
                        tool = Tools(row[6])
                        return [block, player, tool]
    elif options == 0:
        pass
    while True:
        try:
            playername = input("Player Name: ") 
            blockname = input("Block Name: ")
            max = int(input("Block X and Y (Both same as squares): "))
            resource = int(input("Resource Gained From Block: "))
            durabilitytaken = int(input("Durability taken of tool per hit: "))
            toolname = input("Tools: wooden pickaxe, stone pickaxe, iron pickaxe, diamond pickaxe, netherite Pickaxe: ").strip().lower()
            if toolname not in ["wooden pickaxe","stone pickaxe","iron pickaxe","diamond pickaxe","netherite pickaxe"]:
                toolname = input("Tools: wooden pickaxe, stone pickaxe, iron pickaxe, diamond pickaxe, netherite Pickaxe: ").strip().lower()
            block = Block(max, resource, durabilitytaken, blockname)
            player = Player(playername)
            tool = Tools(toolname)
            save.saveparameter(blockname, max, resource, durabilitytaken,playername,toolname)
            option = int(input("Options:\n 1. Add new\n 0. Main Menu: "))
            if option == 1:
                continue
            else:
                return [block, player, tool]
        except ValueError:
            continue


def startgame(block, player, tool, save):
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
                save.savegame(player, block, tool)
                options = int(input((f'Parameters set:\n 1. {player}\n 2. {block}\n 3. {tool}\n Press 1 to continue or 0 to exit main menu: ')))
                if options == 1:
                    continue
                else:
                    return 
        except ValueError:
            continue
def viewprevgames(save):
    save.opensave()
    option = input("Press any key to go back to main menu: ")
    if option == 0:
        return
    else: 
        return




    
    
if __name__ == "__main__":
    main()