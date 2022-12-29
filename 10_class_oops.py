class Employee:
    company="Google"
harry = Employee()
rajni = Employee()    
print(harry.company) #prints google because comany assigned to the employees(harry,rajni)is google 
print(rajni.company)
Employee.company = "youtube"
print(harry.company) #prints youtube because now the company assigned is youtube. 
print(rajni.company)