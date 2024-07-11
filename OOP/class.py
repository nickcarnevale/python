# Class

class MyClass: 
    
    # Constructor

    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)

    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getLength()
    

# Class with multiple constructors
class MyClass2:
    def __init__(self, param1=None, param2=None):
        if param1 is None and param2 is None:
            # Default constructor behavior
            self.param1 = 0
            self.param2 = 0
        elif param1 is not None and param2 is None:
            # Constructor with one parameter
            self.param1 = param1
            self.param2 = 0
        else:
            # Constructor with both parameters
            self.param1 = param1
            self.param2 = param2