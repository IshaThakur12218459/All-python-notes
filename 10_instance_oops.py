class Employee:
    company="Google"
    salary = 100 #this will print incase if there is no salary mentioned in the object.
harry = Employee()
rajni = Employee()
harry.salary = 300
rajni.salary = 400    
print(harry.company) 
print(rajni.company)
print(harry.salary)
print(rajni.salary)#print this salary because the instance program first reads object.