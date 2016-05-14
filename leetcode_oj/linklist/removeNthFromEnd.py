'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
Difficulty: Easy
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, n):
        self.val = x
        self.next = n 

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
	def removeNthFromEnd(self, head, n):
		if not head or n < 1:
			return head
		p1 = p2 = head
		while n != 0:
			if not p1:
				return head
			p1 = p1.next
			n -= 1
		
		
		#If its first element in the list
		if not p1:
			head = head.next
			return head

		while p1.next:
			p1 = p1.next
			p2 = p2.next

		p2.next = p2.next.next
		return head

	def print_list(self, head):
		while head:
			print head.val, "->",
			head = head.next

s = Solution()
a = ListNode(1,
		ListNode(2,
			ListNode(3,
				ListNode(4,
					ListNode(5, None)))))
#s.print_list(s.removeNthFromEnd(a, 2))
#s.print_list(s.removeNthFromEnd(a, 1))
#s.print_list(s.removeNthFromEnd(a, 5))
#s.print_list(s.removeNthFromEnd(a, 15))
b = ListNode(2, None)
#s.print_list(s.removeNthFromEnd(b, 1))
s.print_list(s.removeNthFromEnd(b, 2))
