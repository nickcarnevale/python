# Functions

def func(n, m):
    return n * m

# Nested Functions (Helpful in Recursive functions)

def outer(a,b):
    c = "c"
    def inner():
        return a + b + c
    return inner()

print(outer("a", "b"))


# Can modify objects but cannot reassign values to variables in nested functions
# unless using nonlocal keyword

def double(arr, val):
    
    def helper():
        # modifying array works fine
        for i in range(len(arr)):
            arr[i] *= 2

        # val *= 2 will only modify val in the scope of the helper function
        nonlocal val
        val *= 2

    helper()
    print(arr, val) 

nums = [1, 2]
val = 3
double(nums, val)


        
    



