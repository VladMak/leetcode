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

if __name__ == '__main__':
	solution = Solution()
	#print(solution.twoSum([2,7,11,15], 9))
	#print(solution.twoSum([3,2,4], 6))
	#print(solution.twoSum([3, 3], 6))
	print(solution.reverse(1534236469))