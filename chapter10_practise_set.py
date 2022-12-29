'''Q.1 create a class programmer for storing 
 information of few programmers working at microsoft.'''
# class programmer:
#     company = "Microsoft"

#     def __init__(self, name, product):
#         self.name = name
#         self.product = product

#     def getInfo(self):
#         print(
#             f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")


# harry = programmer("harry", "skype")
# alka = programmer("alka", "github")
# harry.getInfo()
# alka.getInfo()

'''Q.2 Write a class calculator capable of finding
square, cube and squareroot of a number'''
# class Calculator:
#     def __init__(self,num):
#         self.number = num
    
#     def square(self):
#         print(f"the value of {self.number} square is {self.number**2} ")
    
#     def squareRoot(self):
#         print(f"the value of {self.number} squareRoot is {self.number**0.5} ")
    
#     def cube(self):
#         print(f"the value of {self.number} cube is {self.number**3} ")    
# a = Calculator(9)
# a.square()
# a.squareRoot()
# a.cube()

'''create a class with a class attribute a; create 
an object from it and set a directly using object.a = 0
Does this change the class attribute?'''
# class sample:
#     a = "harry"
    
# obj = sample()
# obj.a = "Vicky"
# sample.a = "Vicky"#this will change class attribue.

# print(sample.a)
# print(obj.a)

'''Add a static method in problem 2 to greet the 
user with hello.'''
# class Calculator:
#     def __init__(self,num):
#         self.number = num
    
#     def square(self):
#         print(f"the value of {self.number} square is {self.number**2} ")
    
#     def squareRoot(self):
#         print(f"the value of {self.number} squareRoot is {self.number**0.5} ")
    
#     def cube(self):
#         print(f"the value of {self.number} cube is {self.number**3} ")    

#     @staticmethod
#     def greet():
#         print("*********Hello There**************")

# a = Calculator(9)
# a.square()
# a.squareRoot()
# a.cube()
# a.greet()

'''Write a class train which has methods to book 
a ticket, get status(no. of seats) and get fare
information of trains running under Indian Railways.'''
class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in this train is {self.fare}")
        
    def fareInfo(self):
        print(f"The price of the ticket is : {self.seats}")
    
    def bookticket(self):
        if(self.seats>0):
            print(f"your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
                
        else:
            print("sorry no seats available")
            
            
intercity = Train("Intercity Express:14054", 90, 2)
intercity.getStatus()
intercity.bookticket()
intercity.bookticket()
intercity.bookticket()
