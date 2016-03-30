'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, n):
        self.val = x
        self.next = n

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
	def swapPairs(self, head):
		if not head or not head.next:
			return head
		new_head_next = head.next
		prev = None
		while head:
			#temp = next node in pair
			if not head.next:
				break
			temp = head.next
			#print "Temp.val: ", temp.val
			if prev:
				prev.next = temp
			head.next = temp.next
			#print "Head.val: ", head.val
			temp.next = head 
			prev = head
			head = head.next	
		
		return new_head_next

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
b = ListNode(1, None)
s.print_list(s.swapPairs(b))
