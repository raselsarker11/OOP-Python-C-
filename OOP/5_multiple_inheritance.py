class phone:
    def message(self):
        print("I am inside message")
        
class laptop(phone):
    def browser(self):
        print("I am inside laptop browser")
        
class computer(phone):
    def intel(self):
        print("I am inside intel computer")
        
# class headphone(laptop):
#     def smartphone(self):
#         print("I am inside smartphone device")
        
class desktop(laptop, computer):    
    def programing(self):
        print("I am inside programing laptop and computer")
        

d = desktop()  
d.browser()    
d.message()    
d.programing()    
d.intel() 

