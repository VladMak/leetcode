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

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        """
        ll1 = ListNode(val = 2, next=ListNode(4, next=ListNode(3)))
        while ll1 != None:
            print(ll1.val)
            ll1 = ll1.next
        l1 = list(map(lambda x: str(x), l1[::-1]))
        l2 = list(map(lambda x: str(x), l2[::-1]))
        l1 = "".join(l1)
        l2 = "".join(l2)
        summ = list(str(int(l1) + int(l2)))
        summ = list(map(lambda x: int(x), summ))
        return summ[::-1]

if __name__ == '__main__':
	solution = Solution()
	#print(solution.twoSum([2,7,11,15], 9))
	#print(solution.twoSum([3,2,4], 6))
	#print(solution.twoSum([3, 3], 6))
	solution.addTwoNumbers([2,4,3], [5,6,4])        