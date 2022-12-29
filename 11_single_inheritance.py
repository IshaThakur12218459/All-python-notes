#single inheritance..
class Employee:
    company = "Google"
    
    def ShowDetails(self):
        print("TThis is an employee")
        
class Programmer(Employee):
    language = "Python"
    
    def getLanguage(self):
        print(f"The language is {self.language}")
        
e = Employee()
e.ShowDetails()
p = Programmer()
p.getLanguage()