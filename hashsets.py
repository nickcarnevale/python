# HastSets
# Useful because you can search and insert in constant time
# Duplicates cannot be included in hashset

mySet = set()

mySet.add(1)
mySet.add(2)
mySet.add(3)

print(mySet)
print(len(mySet))

# can search without a function
print(1 in mySet)
print(4 in mySet)

mySet.remove(1)
print(1 in mySet)

# Initalizing

print(set([1,2,3]))

# sets are also initalized with {}
mySet = {i for i in range(5)}
print(mySet)
