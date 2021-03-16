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

    def test_isPalindrome(self):
        """Example 1:

        Input: x = 121
        Output: true

        Example 2:

        Input: x = -121
        Output: false
        Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

        Example 3:

        Input: x = 10
        Output: false
        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

        Example 4:

        Input: x = -101
        Output: false
        """
        self.assertEqual(self.solution.isPalindrome(121), True)
        self.assertEqual(self.solution.isPalindrome(-121), False)
        self.assertEqual(self.solution.isPalindrome(10), False)
        self.assertEqual(self.solution.isPalindrome(-101), False)

    def romanToInt(self):
        """Example 1:

        Input: s = "III"
        Output: 3

        Example 2:

        Input: s = "IV"
        Output: 4

        Example 3:

        Input: s = "IX"
        Output: 9

        Example 4:

        Input: s = "LVIII"
        Output: 58
        Explanation: L = 50, V= 5, III = 3.

        Example 5:

        Input: s = "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
        """
        self.assertEqual(self.solution.romanToInt("III"), 3)
        self.assertEqual(self.solution.romanToInt("IV"), 4)
        self.assertEqual(self.solution.romanToInt("IX"), 9)
        self.assertEqual(self.solution.romanToInt("LVIII"), 58)
        self.assertEqual(self.solution.romanToInt("MCMXCIV"), 1994)

    def test_longestCommonPrefix(self):
        """Example 1:

        Input: strs = ["flower","flow","flight"]
        Output: "fl"

        Example 2:

        Input: strs = ["dog","racecar","car"]
        Output: ""
        Explanation: There is no common prefix among the input strings.
        """
        self.assertEqual(self.solution.longestCommonPrefix(["flower","flow","flight"]), "fl")
        self.assertEqual(self.solution.longestCommonPrefix(["dog","racecar","car"]), "")

    def test_isValid(self):
        """Example 1:

        Input: s = "()"
        Output: true

        Example 2:

        Input: s = "()[]{}"
        Output: true

        Example 3:

        Input: s = "(]"
        Output: false

        Example 4:

        Input: s = "([)]"
        Output: false

        Example 5:

        Input: s = "{[]}"
        Output: true
        """
        self.assertEqual(self.solution.isValid("()"), True)
        self.assertEqual(self.solution.isValid("()[]{}"), True)
        self.assertEqual(self.solution.isValid("(]"), False)
        self.assertEqual(self.solution.isValid("([)]"), False)
        self.assertEqual(self.solution.isValid("{[]}"), True)

    def test_mergeTwoLists(self):
        """Example 1:

        Input: l1 = [1,2,4], l2 = [1,3,4]
        Output: [1,1,2,3,4,4]

        Example 2:

        Input: l1 = [], l2 = []
        Output: []

        Example 3:

        Input: l1 = [], l2 = [0]
        Output: [0]
        """
        self.assertEqual(self.solution.mergeTwoLists("{[]}"), True)
        pass

if __name__ == '__main__':
    unittest.main()