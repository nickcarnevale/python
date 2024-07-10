# Lists (which are just arrays)

arr = [1, 2, 3]
print(arr)

# Other ways of initializing

# initializing an array of size 5 with all values = 1
n = 5
arr = [1] * n
print(n)

# to get the length of array
print(len(arr))

# Be careful when indexing, there is no out of bounds
print(arr[-1]) # prints the last value in arr, -2 would print second to last
 

# Arrays are dynamic in python by default
# They can be used as a stack

arr.append(4)
arr.append(5)
print(arr)

print(arr.pop()) # pop() returns the value popped and gets rid of that value in the array
print(arr)

# Can also insert into an array
arr.insert(1, 7)
print(arr)

# Sublists

arr = [1,2,3,4]
print(arr[1:3]) # prints 2,3, (index 1 to index 3 but not including index 3)

# Unpacking
# how to assign individual elements to arrays
a, b, c = [1, 2, 3] # number of variables needs to match number in array



# Iterating

# Using index
nums = [1,2,3]
for i in range(len(nums)):
    print(nums[1])

# without index
for i in nums:
    print(i)

# Looping through two arrays at the same time
# zip() will stop when the shortest iterable is exhausted. It only includes elements up to the length of the shortest iterable.

nums1 = [1,2,3,4]
nums2 = [4,5,6]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

# Sorting

# ascending order
arr.sort()
# for descending order
arr.sort(reverse=True)

# can also sort strings, by default alphabetical
strings = ["hi", "h", "hello", "alpha"]
strings.sort()
print(strings)

#Custom sort (by length of string for example)
strings.sort(key=lambda x: len(x))
print(strings)

# List comprehension
# fill an array with range()
arr = [i for i in range(5)]
print(arr)

# you can edit perform math on i also
arr = [i+i for i in range(5)]
print(arr)


# Big O
# ------------
# index[]           O(1)
# index assignment  O(1)
# append            O(1)
# pop()             O(1)
# pop(i)            O(n)
# insert(i, item)   O(n)
# del operator      O(n)
# iteration         O(n)
# contains (in)     O(n)
# reverse           O(n)
# sort              O(n log n)
# multiply          O(nm)
# concatenate       O(m)