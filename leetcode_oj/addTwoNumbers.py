'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, n):
		self.val = x
		self.next = n

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
	def addTwoNumbers(self, l1, l2):
		a1 = list()
		a2 = list()
		while(l1):
			a1.insert(0, l1.val)
			l1 = l1.next
		while(l2):
			a2.insert(0, l2.val)
			l2 = l2.next
		if len(a1) > len(a2):
			z = [0] * (len(a1) - len(a2))
			a2 = z + a2
		elif len(a2) > len(a1):
			z = [0] * (len(a2) - len(a1))
			a1 = z + a1
		else:
			pass	
		print "l1: ", a1
		print "l2: ", a2
		result = list()
		c = 0
		for i in range(len(a1) - 1, -1, -1):
			r = a1[i] + a2[i] + c
			if r < 10:
				result.append(r)
				c = 0
			else:
				c = r / 10
				r = r % 10
				result.append(r)
		if c != 0:
			result.append(c)
		print result
		res = None
		prev = None
		for i in range(len(result)):
			new = ListNode(result[i], None)
			if prev != None:
				prev.next = new
			else:
				res = new
			prev = new
		return res

s = Solution()
l1 = ListNode(2,
		ListNode(4,
			ListNode(3, None)))
l2 = ListNode(5,
				ListNode(6,
					ListNode(4, None)))					
'''
l1 = ListNode(1, 
				ListNode(8, None))
l2 = ListNode(0, None)
'''
res = s.addTwoNumbers(l1, l2)
while(res):
	print res.val
	res = res.next
