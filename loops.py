# WHILE LOOPS

n = 0
while n < 5:
    print(n)
    n += 1


# FOR LOOPS
# range(start, stop, step)

# range 0-5 (prints 0,1,2,3,4)
for i in range(5):
    print(i)

# range 2-6 (prints 2,3,4,5)
for i in range(2,6):
    print(i)

n = 5
for i in range(n, 13, 2):
    print(i)

# to go in reverse
# looping from i = 5 to i = 2
for i in range(5, 1, -1):
    print(i)

# decrementing by 2
for i in range(10, 0, -2):
    print(i)


# ITERATING

# Iterating over a list
my_list = [1, 2, 3, 4, 5]
for element in my_list:
    print(element)

# Iterating over a tuple
my_tuple = (10, 20, 30)
for value in my_tuple:
    print(value)

# Iterating over a string
my_string = "Hello"
for char in my_string:
    print(char)

# Iterating over sets
my_set = {1, 2, 3}
for element in my_set:
    print(element)

# Iterating over a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# Enumerating with an Index
my_list = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(my_list):
    print(f"Index {index}: {fruit}")