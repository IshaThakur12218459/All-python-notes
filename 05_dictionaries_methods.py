myDict = {
    "fast": "In a quick manner",
    "harry": "A coder",
    "marks": [1,2,5],
    "anotherdict": {'harry':'player'},           
     1: 2
}
# print(type(myDict.keys( ))) #prints the keys of the dictionaries.
# print(myDict.keys( )) #print the keys
# print(list(myDict.values())) #prints the values of the keys in lists formsn 
# print(myDict.items()) #prints the (key,value)for all the contents in dictionary
updateDict = { 
    "lovish":"Friend"
}   
myDict.update(updateDict) #updates the dictionaries by adding key.value pairs from updateDict.         
# print(myDict)
print(myDict.get("harry")) #returns none if harry2 is not present
print(myDict["harry2"])#throws an error meanwhile .get method does not throwns an error.
  