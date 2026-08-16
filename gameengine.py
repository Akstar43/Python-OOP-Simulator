from save import Save
from player import Player
from block import Block
from tool import Tools
import os
import csv

class GameEngine:
    def __init__(self):
        self.save = Save()
        self.player = None
        self.block = None
        self.tool = None
    def start(self):
        while True:
                try:
                    options = int(input(("Welcome to text based game\n 1. Select Parameters\n 2. Play Game\n 3.  View Pass Games\n 4. Exit\n Option: ")))
                    match(options):
                        case(1):
                            self.selectparams()
                        case (2):
                            if self.block is None:
                                self.selectparams()
                            self.startgame()
                        case (3):
                            self.viewprevgames()
                        case (4):
                            print("Thank you for playing")
                            break
                except ValueError:
                    print("Enter Valid Input")
                    continue
    def selectparams(self):
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
                            self.block = Block(int(row[2]), int(row[3]), int(row[4]), row[1])
                            self.player = Player(row[5])
                            self.tool = Tools(row[6])
                            return
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
                self.block = Block(max, resource, durabilitytaken, blockname)
                self.player = Player(playername)
                self.tool = Tools(toolname)
                self.save.saveparameter(blockname, max, resource, durabilitytaken,playername,toolname)
                option = int(input("Options:\n 1. Add new\n 0. Main Menu: "))
                if option == 1:
                    continue
                else:
                    return
            except ValueError:
                continue


    def startgame(self):
        round = 0
        options = int(input((f'Parameters set:\n 1. {self.player}\n 2. {self.block}\n 3. {self.tool}\n Press 1 to continue or 0 to exit main menu: ')))
        if options == 1:
            pass
        else:
            return
        while self.tool.durability > 0:
            try:
                mine = input("Type 'mine' to mine or exit to go back to main menu: ").lower().strip()
                if mine == "mine":
                    self.block.renderblock()
                    self.block.damage(self.tool.damage)
                    self.tool.tooldamage(self.block.durabilitytaken)
                    if self.block.blockbroken():
                        print("Block Broken")
                        self.player.gain(self.block.resource)
                        print(f'Player Inventory: {self.player.playerinventory}')
                        self.block.regenerate()
                        round += 1
                elif mine == "exit":
                    self.save.savegame(self.player, self.block, self.tool)
                    options = int(input((f'Parameters set:\n 1. {self.player}\n 2. {self.block}\n 3. {self.tool}\n Press 1 to continue or 0 to exit main menu: ')))
                    if options == 1:
                        continue
                    else:
                        return 
            except ValueError:
                continue
    def viewprevgames(self):
        self.save.opensave()
        option = input("Press any key to go back to main menu: ")
        if option == 0:
            return
        else: 
            return
           



    
    

