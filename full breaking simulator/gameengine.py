from save import Save
from player import Player
from block import Block
from tool import Tools
from load import Load
import os
import csv
from ui import UI

class GameEngine:
    def __init__(self):
        self.save = Save()
        self.player = None
        self.block = None
        self.tool = None
        self.ui = UI()
    def start(self):
        while True:
                try:
                    options = int(input(self.ui.options()))
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
                            print(self.ui.thankyou())
                            break
                except ValueError:
                    print(self.ui.errormsg())
                    continue
    def selectparams(self):
        options = int(input(self.ui.option1ui1()))
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
                playername = input(self.ui.playernameselect()) 
                blockname = input(self.ui.blockselect())
                max = int(input(self.ui.blocksizeselect()))
                resource = int(input(self.ui.blockresourceselect()))
                durabilitytaken = int(input(self.ui.tooldurabilityselect()))
                toolname = input(self.ui.toolparamselect()).strip().lower()
                if toolname not in [self.ui.toolparamcondition()]:
                    toolname = input(self.ui.toolparamselect()).strip().lower()
                self.block = Block(max, resource, durabilitytaken, blockname)
                self.player = Player(playername)
                self.tool = Tools(toolname)
                self.save.saveparameter(blockname, max, resource, durabilitytaken,playername,toolname)
                option = int(input(self.ui.option1ui2()))
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
                mine = input(self.ui.mineui()).lower().strip()
                if mine == "mine":
                    self.gameplayhelper()
                    if self.block.blockbroken():
                        self.gameplayhelper2()
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
        option = input(self.ui.option3ui1())
        if option == 0:
            return
        else: 
            return
    def gameplayhelper(self):
        self.block.renderblock()
        self.block.damage(self.tool.damage)
        self.tool.tooldamage(self.block.durabilitytaken)
    def gameplayhelper2(self):
        print(self.ui.blockbrokenui())
        self.player.gain(self.block.resource)
        print(f'Player Inventory: {self.player.playerinventory}')
        self.block.regenerate()

           



    
    

