class Employee:
    company="Google"
    def getsalary(self, signature):#self is a parameter that passes automatically in any function
        print(f"salary for this employee working in {self.company} is {self.salary}\n{signature}")
    @staticmethod
    def greet():
        print("Good morning, sir")    
harry = Employee()
harry.salary = 100000
harry.getsalary("thanks!")
harry.greet()