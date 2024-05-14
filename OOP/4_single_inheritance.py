

class plane:
    def __init__(self, name, color, brand, price):
        self.name = name
        self.color = color
        self.brand = brand
        self.price = price
        
    def printall(self):
        print(self.name, self.color, self.brand, self.price)
        
my_plane = plane("Rasel sarker", "Red", "chanku pankhu", "1478963")
my_plane.printall()