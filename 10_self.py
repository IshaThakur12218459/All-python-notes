class Employee:
    company="Google"
    def getsalary(self):#self is a parameter that passes automatically in any function
        print(f"salary for this employee working in {self.company} is {self.salary}")
        
harry = Employee()
harry.salary = 100000
harry.getsalary() #Employee.gtesalary(harry)-->both has same meaning