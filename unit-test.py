import unittest

# Assume MyClass and MyClass2 are already defined as in your previous code

class TestMyClasses(unittest.TestCase):
    
    def test_MyClass(self):
        nums = [1, 2, 3, 4, 5]
        obj = MyClass(nums)
        
        # Test getLength()
        self.assertTrue(obj.getLength() == len(nums), "getLength() should return the correct length")
        
        # Test getDoubleLength()
        self.assertTrue(obj.getDoubleLength() == 2 * len(nums), "getDoubleLength() should return double the length")
        
    def test_MyClass2(self):
        # Test default constructor
        obj1 = MyClass2()
        self.assertTrue(obj1.param1 == 0 and obj1.param2 == 0, "Default constructor should initialize params to 0")
        
        # Test constructor with one parameter
        obj2 = MyClass2(10)
        self.assertTrue(obj2.param1 == 10 and obj2.param2 == 0, "One parameter constructor should set param1 correctly and param2 to 0")
        
        # Test constructor with two parameters
        obj3 = MyClass2(10, 20)
        self.assertTrue(obj3.param1 == 10 and obj3.param2 == 20, "Two parameters constructor should set both param1 and param2 correctly")

if __name__ == '__main__':
    unittest.main()


# assertEqual(a, b, msg=None)
# Asserts that a == b.
# Example: self.assertEqual(2 + 2, 4)
# assertNotEqual(a, b, msg=None)

# Asserts that a != b.
# Example: self.assertNotEqual(2 + 2, 5)
# assertTrue(x, msg=None)

# Asserts that bool(x) is True.
# Example: self.assertTrue(4 > 0)
# assertFalse(x, msg=None)

# Asserts that bool(x) is False.
# Example: self.assertFalse(4 < 0)
# assertIs(a, b, msg=None)

# Asserts that a is b (checks for object identity).
# Example: self.assertIs(None, None)
# assertIsNot(a, b, msg=None)

# Asserts that a is not b.
# Example: self.assertIsNot(a, b) where a and b are different objects.
# assertIsNone(x, msg=None)

# Asserts that x is None.
# Example: self.assertIsNone(None)
# assertIsNotNone(x, msg=None)

# Asserts that x is not None.
# Example: self.assertIsNotNone(5)
# assertIn(a, b, msg=None)

# Asserts that a is in b (where b is a sequence, string, etc.).
# Example: self.assertIn(3, [1, 2, 3])
# assertNotIn(a, b, msg=None)

# Asserts that a is not in b.
# Example: self.assertNotIn(4, [1, 2, 3])