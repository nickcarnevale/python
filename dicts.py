# Hashmaps (dictionary aka dicts)

myMap = {}

# 88 is the value mapped to the key alice
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)

myMap["alice"] = 80
print(myMap["alice"])

var = "alice" in myMap
print(var)

myMap.pop("alice")
print("alice" in myMap)

# Initalizing
myMap = {"alice": 80, "bob": 90}
print(myMap)

# Dict comprehension
myMap = {i: 2*i for i in range(5)}
print(myMap) # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# Looping through dicts

myMap = {"alice": 80, "bob": 90}
for key in myMap:
    print(f"{key}: {myMap[key]}")

for val in myMap.values():
    print(val)

for key, val in myMap.items(): 
    print(key, val)

