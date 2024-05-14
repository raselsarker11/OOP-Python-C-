

class phone:
    def __init__(self, name, color, price, brand, model):
        self.name = name
        self.color = color
        self.price = price
        self.brand = brand
        self.model = model
        
    def mobile_phone(self):
        print("Awesome Mobile Phone")
        
        
class car:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        
        
    def private_car(self):
        print("Awesome Private Car")
        
my_phone = phone("Iphone15 pro", "gold", "1458", "Apple", "Apple 14")
print(my_phone)


my_car = car("Tasla", "red", "147896")
print(my_car)

