'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
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
	def mergeTwoLists(self, l1, l2):
		l = ListNode(None, None)
		head = l
		while l1 and l2:
			if l1.val < l2.val:
				l.next = l1
				l1 = l1.next
			elif l2.val < l1.val:
				l.next = l2
				l2 = l2.next
			else:
				l.next = l1
				l1 = l1.next
				l = l.next
				l.next = l2
				l2 = l2.next
			l = l.next
		
		if l1:
			while l1:
				l.next = l1
				l = l.next
				l1 = l1.next
		if l2:
			while l2:
				l.next = l2
				l = l.next
				l2 = l2.next
		return head.next

s = Solution()
l1 = ListNode(7,
		ListNode(10,
			ListNode(12,
				ListNode(15, None))))
l2 = ListNode(1,
		ListNode(4,
			ListNode(9,None)))
l3 = ListNode(13, None)
l4 = ListNode(13, None)
l = s.mergeTwoLists(l4, l3)
while l:
	l = l.next
