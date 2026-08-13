class Tools:
    def __init__(self, tool):
        self.tool = tool
    def __str__(self):
        return self.tool
    @property
    def damage(self):
        return self._damage
    @damage.setter
    def damage(self, damage):
        self._damage = damage
    @property
    def durability(self):
        return self._durability
    @durability.setter
    def durability(self, durability):
        if durability <= 0:
            durability = 0
        self._durability = durability
    @property
    def tool(self):
        return self._tool
    @tool.setter
    def tool(self, tool):
        if tool == "wooden pickaxe":
            self.damage = 1
            self.durability = 69
        if tool == "stone pickaxe":
            self.damage = 2
            self.durability = 139
        if tool == "iron pickaxe":
            self.damage = 12
            self.durability = 32
        if tool == "diamond pickaxe":
            self.damage = 8
            self.durability = 1561
        if tool == "netherite pickaxe":
            self.durability = 2031
            self.damage = 10
        self._tool = tool
    def tooldamage(self, n):
        self.durability -= n
    def toolbroken(self):
        if self.durability <= 0:
            return True
        return False