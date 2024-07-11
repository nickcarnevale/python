# Tuples are like arrays but they are immutable

tup = (1,2,3)
print(tup)
print(tup[0])
print(tup[-1])

# Can index but cannot modify tuples

# Tuples can be used as a key in a hash map/set
# Lists on the other hand cannot be keys
myMap = {(1,2): 3}
print(myMap[(1,2)]) 

mySet = set()
mySet.add((1,2))
print((1,2) in mySet)


