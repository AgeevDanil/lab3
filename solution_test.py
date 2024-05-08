import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
 
    def setUp(self):
        self.sol = Solution()   
    def test_quicksort(self):
        result = self.sol.quicksort([3,1,5,2])
        self.assertEqual(result,[1,2,3,5])

if __name__ == '__main__':
    unittest.main()