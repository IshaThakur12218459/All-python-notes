class Employee:
    company="Google"
    
    def __init__(self, name, salary, subunit): #init is a constructor method
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")
        
    
    def getDetail(self):#self is a parameter that passes automatically in any function
        print(f"the name of the employee is {self.name}")
        print(f"the salary of the employee is {self.salary}")
        print(f"the subunit of the employee is {self.subunit}")

        
harry = Employee("Harry", 1000, "printers")
harry.getDetail()
