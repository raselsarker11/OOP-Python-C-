
class Person:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
        
    def __str__(self) -> str:
        return f"My name is {self.name}, I am {self.age} years old, and I work in {self.department}."
    
    
    def __del__(self): # destructor name is also same as class name
        print("I am Destructor")
    
# Create an instance of the Person class
person2 = Person("Rasel Sarker", 36, "Computer Science")

# Print out attributes of the person
print(person2.name)
print(person2.age)
print(person2.department)


print(str(person2)) #Print out a descriptive string representation of the person


# Now, let's delete the person2 object
del person2
