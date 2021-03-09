from ListNode import ListNode

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
    	"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

		You may assume that each input would have exactly one solution, and you may not use the same element twice.

		You can return the answer in any order.		
    	"""
    	for i, j in enumerate(nums):
    		for k, n in enumerate(nums):
    			if i == k:
    				continue
    			else:
    				if j + n == target:
    					return [i, k]

    def reverse(self, x: int) -> int:
        """Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

        Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
        """
        if x >= 0:
            return 0 if int(str(x)[::-1]) < -2147483648 or int(str(x)[::-1]) > 2147483647 else int(str(x)[::-1])
        else:
            return 0 if -int(str(x).replace("-", "")[::-1]) < -2147483648 or -int(str(x).replace("-", "")[::-1]) > 2147483647 else -int(str(x).replace("-", "")[::-1])

    def isPalindrome(self, x: int) -> bool:
        """Given an integer x, return true if x is palindrome integer.

        An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
        """
        if str(x) == str(x)[::-1]:
            return True
        return False

    def romanToInt(self, s: str) -> int:
        """Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000

        For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

        Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.

        Given a roman numeral, convert it to an integer.
        """
        symbols = dict(I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000)
        number = 0
        last_num = 0
        for num in s:
            if last_num >= symbols[num]:
                last_num = symbols[num]
                number += symbols[num]
            else:
                number += symbols[num] - last_num - last_num
                last_num = symbols[num]
        return number

    def longestCommonPrefix(self, strs: list) -> str:
        """Write a function to find the longest common prefix string amongst an array of strings.

        If there is no common prefix, return an empty string "".
        """
        prefix = ""
        if strs and len(strs) > 1:
            last_pref = strs[0]
            for word in strs[1:]:
                prefix += "_"
                #breakpoint()
                if len(last_pref) >= len(word):
                    for k, v in enumerate(word):
                        if v == last_pref[k]:
                            prefix += v
                        else:
                            last_pref = prefix
                            break
                else:
                    for k, v in enumerate(last_pref):
                        if v == word[k]:
                            prefix += v
                        else:
                            last_pref = prefix
                            break
                last_pref = prefix.split("_")[-1]
        elif len(strs) == 1:
            return strs[0]

        return prefix.split("_")[-1]

if __name__ == '__main__':
	solution = Solution()
	#print(solution.twoSum([2,7,11,15], 9))
	#print(solution.twoSum([3,2,4], 6))
	#print(solution.twoSum([3, 3], 6))
	print(solution.longestCommonPrefix(["aaa","aa","aaa"]))