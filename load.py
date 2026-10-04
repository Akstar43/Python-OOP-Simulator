import json
class Load:
    def __init__(self):
        self.loadblock = 'blocks.json'
        self.loadtools = 'toools.json'
        self.blocks = self.loadexistingjson()
    def loadexistingjson(self):
        try: 
            with open('blocks.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
                
    def addnewblock(self):
        while True:
            try:
                blockname = input("Enter new block name: ")
                durabilitytaken = int(input("durability taken: "))
                size = int(input("Block size"))
                resource = int(input("Resource gained"))
                options = int(input("1. continue 2. save:"))
            except ValueError:
                continue
            self.blocks.append({"block name": blockname, "durabilitytaken": durabilitytaken,"size": size, "resource": resource})
            if options == 1:
                continue
            elif options == 2:
                self.loadblocks()
                break

    def saveblocks(self):
        with open('blocks.json', "w") as File:
            json.dump(self.blocks, File, indent=4)
                
    

