# Parent class 1
class Subject:
    def __init__(self, name):
        self.name = name
        
    def display(self):
        print(f"Subject Name: {self.name}")
   
   
# Parent class 2     
class Department:
    def __init__(self, cse):
        self.cse = cse

    def display(self):
        print(f"Department Name: {self.cse}")


# Child class inheriting 
class SubjectDepartment(Subject, Department):
    def __init__(self, name, cse):
        Subject.__init__(self, name)
        Department.__init__(self, cse)

    def display_info(self):
        self.display()
        self.display_name()


my_subject_department = SubjectDepartment("Chemistry", "CSE")

my_subject_department.display_info()
