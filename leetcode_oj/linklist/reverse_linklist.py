# Definition for singly-linked list.
class ListNode:
	def __init__(self, x, n):
         self.val = x
         self.next = n

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
		self.reverse_list_helper(head)
		return head

    def reverse_list_helper(self, head):
		if head == None:
			return
		rest = head.next
		if (not rest):
			return
		print "***"
		print "Before assignment: "
		try:
			print "head.val: ", head.val
		except:
			print "None"
		try:
			print "head.next.val: ", head.next.val
		except:
			print "None"
		self.reverse_list_helper(rest)
		head.next.next = head
		head.next = None
		head = rest
		'''
		try:
			print "Head.next.next.val: ", head.next.next.val
		except:
			print "None"
		try:
			print "head.next.val: ", head.next.val
		except:
			print "None"
		try:
			print "rest.val: ", rest.val
		except:
			print "None"
		'''
		print "***"
		print "After assignment: "
		try:
			print "head.val: ", head.val
		except:
			print "None"
		try:
			print "head.next.val: ", head.next.val
		except:
			print "None"
	
def print_list(n):
	while(n):
		print n.val
		n = n.next
n5 = ListNode(5, None)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

s = Solution()
s.reverseList(n1)
print_list(n1)
