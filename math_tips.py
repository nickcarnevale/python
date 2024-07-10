# MATH

# DIVISION
# Division is decimal by default
print(5/2)      # prints 2.5

# Integer division is "//"
print (5//2)    # prints 2

# CAREFUL: python // will round down, not to 0
print (-3//2)   # prints -2

# workaround, convert the decimal to an int
print(int(-3/2))  # prints -1   

# MODULUS
# positive modding is similiar
print(10 % 3) # prints 1

# negative modding gives unexpected values
print(-10 % 3) #prints 2

# workaround
import math
print(math.fmod(-10, 3)) #prints -1

# useful math helpers

#round down
print(math.floor(3/2))

#round up
print(math.ceil(3/2))

#square root
print(math.sqrt(2))

#2^3
print(math.pow(2,3))


#MAX INTEGER
float("inf")

#MIN INTEGER
float("-inf")

# python numbers are infinite so they never overflow
print(math.pow(2,300))

#but they never overflow
print(math.pow(2,300) < float("inf"))