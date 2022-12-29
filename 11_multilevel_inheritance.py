class Person:
    country = "India"
    
    def takeBreak(self):
        print("breath")
        
class Employee(Person):
    company = "honda"
    
    def getSalary(self):
        print(f"salary is {self.salary}")
        
    def takebreak(self):
        print("i am breathing..")
            
class Programmer(Employee):
    company = "Fiverr"
    
p = Person()
e = Employee()
pr = Programmer()
p.takeBreak()
e.takeBreak()
