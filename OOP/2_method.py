
#========================================================================================
# Methods: Methods are functions that are associated with an object or a class.
#========================================================================================
#There are basically three types of methods in Python:
#       1.Instance Method.
#       2.Class Method.
#       3.Static Method.



class Car:
    value = 100000  # Class attribute

def display(self):
    print("Tesla car")

    obj = Car()
    print(Car.__dict__)

