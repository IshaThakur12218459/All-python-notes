b = set()
#adding values to empty sets.
b.add(4)
b.add(5)
b.add(9)
b.add(8)
# print((b))
#cannot add list but can add tuples.neither dictionary because they are not hashable.
#it means if it can be changed then it can not be added to sets.
# print(b)
# print(len(b))#prints the length of the sets.
# b.remove(5)#removes 5 from set
# print(b)
# print(b.pop())#it will remove anyrandom number.
# print(b)
print(b.union({8,11}))
print(b.intersection({8,11}))