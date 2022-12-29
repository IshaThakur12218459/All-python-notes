# i = 4
# if i>0:
#     pass
# print("something")

#practise set
#Q.1
num = int(input("Enter a number: "))
for i in range(1,11):
    #print(str(num) +  " X "  +  str(i) +  " = "  + str(i*num) ) 
    print(f"{num} X {i} = {num*i}")   #f is known as f string..
    


#Q.2
# l1 = ["Harry", "Sohan", "Sachin", "rahul"]
# for name in l1:
#     if name.startswith("S"):
#         print("Hello " + name )

#Q.3
# num = int(input("Enter rhe number: "))
# prime = True
# for i in range(2, num):
#     if(num%i == 0):
#         prime = False
#         break
# if prime:        
#     print("This number is prime") 
# else:
#     print("This is not prime") 

#Q.4
# num = int(input("Enter rhe number: "))
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial * i
# print(f"THe factorial of this {num} is {factorial}")     


#Q.5
# n = 4
# for i in range(4):
#     print("*" * (i+1))


#Q.6
# n = 3
# for i in range(3):
#     print(" " * (n-i-1), end="")
#     print("*" * (2*i+1), end="")
#     print(" " * (n-i-1))