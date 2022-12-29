# Q.1
myDict = {
    "pankha": "fan",
    "dabba":"box",
    "vastu":"items"
}
print("options are",myDict.keys())
a = input("Enter the hindi word\n")
print("the meaning of your word is: ",myDict[a])
#below line will not throw an error if word is not present in the dictionary.
print("the meaning of your word is: ",myDict.get(a))


# Q.2
num1 = int(input("Enter a number 1\n"))
num2 = int(input("Enter a number 2\n"))
num3 = int(input("Enter a number 3\n"))
num4 = int(input("Enter a number 4\n"))
num5 = int(input("Enter a number 5\n"))
num6 = int(input("Enter a number 6\n"))
num7 = int(input("Enter a number 7\n"))
num8 = int(input("Enter a number 8\n"))

s = {num1,num2,num3,num4,num5,num6,num7,num8}
print(s)

# Q.3
s = {18 , "18" , 18.1}
print(s)

# Q.4
s = set()
s.add(20)
s.add(20.0)#20 & 20.0 is counted same in python.beacuse it has same value. 
s.add("20")
print(len(s))


# Q.5
favlang = {}
a = input("Enter your favourite language X\n ") 
b = input("Enter your favourite language Y\n ")
c = input("Enter your favourite language Z\n ")
d = input("Enter your favourite language F\n ")
favlang['X'] = a
favlang['Y'] = b
favlang['Z'] = c
favlang['F'] = d
print(favlang)

