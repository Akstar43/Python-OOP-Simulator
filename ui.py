class UI:
    #main ui
    def options(self):
        return "Welcome to text based game\n 1. Select Parameters\n 2. Play Game\n 3.  View Pass Games\n 4. Add new block, tools\n 5. Exit\n Option: "
    def thankyou():
        return "Thank you for playing"
    def errormsg():
        return "Enter Valid Input"
    #option 1
    def option1ui1(self):
        return "1. Load from save 0. Add new Parameters 2. Load Predefined params: "
    #option 1 select game elements
    def toolparamselect(self):
        return "Tools: wooden pickaxe, stone pickaxe, iron pickaxe, diamond pickaxe, netherite Pickaxe: "
    def toolparamcondition(self):
        return "wooden pickaxe","stone pickaxe","iron pickaxe","diamond pickaxe","netherite pickaxe"
    def playernameselect(self):
        return "Player Name: "
    def blockselect(self):
        return "Block Name: "
    def blocksizeselect(self):
        return "Block X and Y (Both same as squares): "
    def blockresourceselect(self):
        return "Resource Gained From Block: "
    def tooldurabilityselect(self):
        return "Durability taken of tool per hit: "
    def option1ui2(self):
        return "Options:\n 1. Add new\n 0. Main Menu: "
    #playgame
    def mineui(self):
        return "Type 'mine' to mine or exit to go back to main menu: "
    def blockbrokenui(self):
        return "Block Broken"
    def option3ui1(self):
        return "Press any key to go back to main menu: "
    
    