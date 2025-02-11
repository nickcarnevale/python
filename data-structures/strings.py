# Strings

# Strings are similar to arrays
s = "abc"
print(s[0:2])

# trim a string
stri = "    hi"
s = stri.strip()
print(s)

# This will create a new string "end time operation"
s += "def"

# valid numeric strings can be converted to integers
print(int("123") + int("123"))
print(str(123) + str(123))

# if you need the ascii value of a char
print(ord("a"))
print(ord("b"))

# combining a list of strings
strings = ["ab", "cd", "ef"]
string = "".join(strings)
print(f"This is the string: {string}")

# iterating a strings
for c in string:
    print(c)

for i in range(len(string)):
    print(f"{i}: {string[i]}")