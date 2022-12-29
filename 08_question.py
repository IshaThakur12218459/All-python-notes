#Q.1
# def maximum(num1, num2, num3):
#     if (num1>num2):
#         if(num1>num3):
#             return num1 
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3
# m = maximum(3, 5, 7)
# print("The maximum number is " + str(m))            

#Q.2
# def farh(cel):
#     return (cel * 9/5) + 32

# c = 0
# f = farh(c)
# print("Fahrenheit temperature is " + str(f))
    
#Q.3
# print("hello", end=" ")    
# print("how", end=" ")    
# print("are", end=" ")    
# print("you?", end=" ")    


#Q.4
# n = 3
# for i in range(n):
#     print("*" * (n-i))

#Q.5
def remove_and_split(string,word):
    newstr = string.replace(word, "")
    return newstr.strip()
this = "    Harry is good    "
n = remove_and_split(this,"Harry")
print(n)