class Block: 
    def __init__(self, max, resource, durabilitytaken, name):
        self.name = name
        self.max = max
        self.height = self.max
        self.width = self.max
        self.resource =  resource
        self.min = 0
        self.durabilitytaken = durabilitytaken
    def __str__(self):
        return f'Block Name: {self.name}, Block Size: {self.height}, Block Resource: {self.resource},Block Durability Taken: {self.durabilitytaken}'
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height):
        if height <= 0:
            height = 0
        self._height = height
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, width):
        if width <= 0:
            width = 0
        self._width = width
    def damage(self, n):
        self.height -= n
        self.width -= n
    def renderblock(self):
        brick = "🧱" * self.width
        print(f'{brick}\n' * self.height)
    def blockbroken(self):
        if self.height <= 0 or self.width <= 0:
            return True
        return False
    def regenerate(self):
        self.height = self.max
        self.width = self.max
        