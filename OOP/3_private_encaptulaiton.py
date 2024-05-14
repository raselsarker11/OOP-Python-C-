

# PRIVATE METHODS

class Car:
    def __init__(self, make, model):
        self.__make = make  # private attribute
        self.__model = model 

    def __update_model(self, new_model): 
        self.__model = new_model

    def get_make(self): 
        return self.__make

    def set_model(self, new_model):  
        self.__update_model(new_model)

    def get_model(self):
        return self.__model


my_car = Car("Tasla", "BMW")
print(my_car.get_make())  
my_car.set_model("Ferrari")
print(my_car.get_make())  



# public attribute

class teacher:
    def __init__(self, name, age, dept, phone):
        self._name = name
        self._age = age
        self._dept = dept
        self._phone = phone 
        
    def __newteacher(self, name): 
        self._name = name
        

teacher_instance = teacher("Rahim", 40, "CSE", "01581528651") 

print(teacher_instance._name) 
print(teacher_instance._age) 
print(teacher_instance._dept) 
print(teacher_instance._phone) 

 