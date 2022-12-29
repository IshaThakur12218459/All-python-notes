#Q.1
# num1 = int(input("Enter a number 1: "))
# num2 = int(input("Enter a number 2: "))
# num3 = int(input("Enter a number 3: "))
# num4 = int(input("Enter a number 4: "))

# if(num1>num4):
#     f1 = num1
# else:
#     f1 = num4  
# if(num2>num3):
#     f2 = num2
# else:
#     f2 = num3    
# if(f1>f2):
#     print(f1, "f1 is the largest")
# else:
#     print(f2, "f2 is the largest")             

# Q.2
# sub1 = int(input("Enter first subject marks\n"))
# sub2 = int(input("Enter second subject marks\n"))
# sub3 = int(input("Enter third subject marks\n"))

# if(sub1<33 or sub2<33 or sub3<33):
#     print("You are fail.")
# elif(sub1+sub2+sub3)/3 <40:
#     print("You are fail due to total percentage less than 40.")     
# else:
#     print("you pass the exam")    

# Q.3 
# text = (input("Enter the text\n"))

# if("make a lot of money" in text):
#     spam = True
# elif("buy now"in text):
#     spam = True    
# elif("subscribe this"in text):
#     spam = True       
# elif("click this"in text):
#     spam = True  
# else:
#     spam = False    
# if(spam):
#     print("This is spam")         
# else:
#     print("This is not a spam")    

#Q.4
marks = int(input("Enter your marks\n"))

if marks>=90:
    grade = "Ex"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D"                
else:
    grade = "F"
print("Your grade is " + grade)    
    
        
    