import unittest
from main import Solution 
from ListNode import ListNode

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

    def test_addTwoNumbers(self):
        """Example 1:

        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.

        Example 2:

        Input: l1 = [0], l2 = [0]
        Output: [0]

        Example 3:

        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,9,9,0,0,0,1]
        """
        l1 = ListNode(val = 2, next=ListNode(4, next=ListNode(3)))
        self.assertEqual(self.solution.addTwoNumbers([2,4,3], [5,6,4]), [7,0,8])
        self.assertEqual(self.solution.addTwoNumbers([0], [0]), [0])
        self.assertEqual(self.solution.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]), [8,9,9,9,0,0,0,1])

if __name__ == '__main__':
    unittest.main()