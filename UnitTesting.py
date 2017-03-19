import unittest

def sort_negative_remove(ls):
    """ Sort and Remove Negative values from a list."""
    l = [i for i in ls if i > 0]
    return sorted(l)

class TestMethods(unittest.TestCase):
    """Methods to Test, Implements unittest Testcase Class"""
    def test1(self):
        """Test 1"""
        ls = [2, 7, -2, -3 ,-67, 22, 4 , -55]
        self.assertEqual(sort_negative_remove(ls), [2, 4, 7, 22])

    def test2(self):
        """Test 2"""
        ls = [2,3,4,5,-1,1,-3,6,-10]
        self.assertEqual(sort_negative_remove(ls), [1,2,3,4,5,6])

if __name__ == "__main__":
    unittest.main()
