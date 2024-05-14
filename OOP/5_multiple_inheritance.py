class Car:
    num_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        
        Car.num_cars += 1 # Incrementing the class attribute

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")

    @classmethod
    def display_num_cars(cls):
        print(f"Number of cars: {cls.num_cars}")



car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model S")


car1.display_info()  
car2.display_info() 
Car.display_num_cars() 
