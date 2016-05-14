'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
 Linked List
Hide Similar Problems (E) Remove Element (E) Delete Node in a Linked List
Difficulty: Easy
'''
class ListNode:
	def __init__(self, x, n):
		self.val = x
		self.next = n

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
	def removeElements(self, head, val):
		prev = None
		curr = head
		while curr:
			if curr.val == val:
				if prev:
					prev.next = curr.next
				else:
					head = curr.next
			else:
				prev = curr
			curr = curr.next
		return head

def print_list(head):
	while head:
		print head.val, "-->"
		head = head.next

n6 = ListNode(1, None)
n5 = ListNode(5, n6)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n62 = ListNode(6, n3)
n2 = ListNode(1, n62)
n1 = ListNode(1, n2)

s = Solution()
head = s.removeElements(n6, 1)
print_list(head)
