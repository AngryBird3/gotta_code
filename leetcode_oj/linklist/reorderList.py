'''
Given a singly linked list L: L0 L1 ... Ln-1 Ln,
reorder it to: L0 Ln L1 Ln-1 L2 Ln-2 -...
You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def reorderList(self, head):
		"""
		:type head: ListNode
		:rtype: void Do not return anything, modify head in-place instead.
		"""
		'''
		Algorithm:

		l0 l1 l2 l3 l4 l5 l6 l7
		1) Find middle element : l3
		2) Reverse last half:
			l0 l1 l2 l3   l7 l6 l5
		3) Some how join how it requires!
		'''
		if not head:
			return
		#Find middle element
		slow = head
		fast = head
		
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		#Reverse second half
		middle = slow
		cur = slow
		prev = None
		while cur:
			rest = cur.next
			cur.next = prev
			prev = cur
			cur = rest
		
		#Combine l1 (head) and l2 (rev half)
		l2 = prev	
		l1 = head
		while l1 != middle:
			print "l1.val: ", l1.val
			print "middle.val: ", middle.val
			print "l2.val: ", l2.val
			temp1 = l1.next
			l1.next = l2
			temp2 = l2.next
			l2.next = temp1
			l2 = temp2
			l1 = temp1
		l1.next = None
		

s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2; l2.next = l3; l3.next = l4; l4.next = l5;
s.reorderList(l1)
while l1:
	print l1.val,
	l1 = l1.next
