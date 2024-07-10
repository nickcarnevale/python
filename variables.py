#Variables

# Variables are dynamicaly typed
# This means types are determined at runtime

n = 0
print('n = ', n)

n = "abc"
print('n = ', n)

# Multiple assignments
n, m = 0, "abc"

n, m, z = 0.125, "abc", False

# Incrementing
n = n + 1
n += 1

# n++ not allowed

# None is null (absence of value)

n = 4
n = None
print('n = ', n)