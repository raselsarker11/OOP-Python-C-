#=========================================================================================
# Inheritance is a method in which the properties of one class are carried over to another class.
#=========================================================================================


class phone:
    def call(self):
        print("Calling phone")
        
    def message(self):
        print("Message received successfully")
        
        
class laptop(phone):
    def phone(self):
        print("Calling laptop successfully")
        
p = laptop()
p.call()
p.message()
p.phone()



############################################################

class A:
    pass
class B(A):
    pass
class C(A, B):
    pass