f = open('sample.txt','r')
#reads first line
data = f.readline()
print(data)
#reads second line
data = f.readline()
print(data)
# reads third line
data = f.readline()
print(data)
#and so on...
data = f.readline()
print(data)
f.close()