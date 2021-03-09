import unittest
from main import Solution 

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_twoSum(self):
        """Example 1:

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Output: Because nums[0] + nums[1] == 9, we return [0, 1].

        Example 2:

        Input: nums = [3,2,4], target = 6
        Output: [1,2]

        Example 3:

        Input: nums = [3,3], target = 6
        Output: [0,1]
        """
        self.assertEqual(self.solution.twoSum([2,7,11,15], 9), [0, 1])
        self.assertEqual(self.solution.twoSum([3,2,4], 6), [1, 2])
        self.assertEqual(self.solution.twoSum([3, 3], 6), [0, 1])

    def test_reverse(self):
        """Example 1:

        Input: x = 123
        Output: 321

        Example 2:

        Input: x = -123
        Output: -321

        Example 3:

        Input: x = 120
        Output: 21

        Example 4:

        Input: x = 0
        Output: 0
        """
        self.assertEqual(self.solution.reverse(123), 321)
        self.assertEqual(self.solution.reverse(-123), -321)
        self.assertEqual(self.solution.reverse(120), 21)
        self.assertEqual(self.solution.reverse(0), 0)

if __name__ == '__main__':
    unittest.main()