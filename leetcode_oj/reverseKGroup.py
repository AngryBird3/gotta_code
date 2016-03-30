'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def reverseKGroup(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		
		''' 
		Algorithm:

		- I can reverse k at a time: pieace of cake?
		- How do I keep track whether the "next chunk" has k nodes?
		- 	So to find that: use next_ptr:
				- while working on current reverse, advance 
				- next_ptr to "next chunk"'s kth node - as in head/tail
				- head after reverse, tail for now
		'''

		if not head or k < 2:
			return head

		#Finding our 1st next_ptr
		next_ptr = head
		for i in range(k-1):
			if next_ptr:
				next_ptr = next_ptr.next
			else:
				#Base case, when we don't have in first chunk k node
				return head

		new_head = next_ptr
		if not new_head:
			return head
		cur = head
		while next_ptr:
			#Reverse cur chunk and find tail for next chunk
			rev = None
			tail = cur
			for i in range(k):
				#Get next_ptr set
				if next_ptr:
					next_ptr = next_ptr.next
					
				nxt = cur.next
				cur.next = rev	
				rev = cur
				cur = nxt
			
			tail.next = cur
			if next_ptr:
				tail.next = next_ptr
			
		return new_head

s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2; l2.next = l3; l3.next = l4; l4.next = l5
ret = s.reverseKGroup(l1, 6)
while ret:
	print ret.val,	
	ret = ret.next
print ''
