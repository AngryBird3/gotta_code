'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, n):
        self.val = x
        self.next = n

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
	def deleteDuplicates(self, head):
		res = head
		prev_l = res
		prev_v = res.val
		head = head.next
		while head:
			print "head.val: ", head.val, " prev_v: ", prev_v, "prev_l.val: ", prev_l.val
			if head.val == prev_v:
				pass
			else:
				prev_l.next = head
				prev_l = prev_l.next
				prev_v = head.val
			head = head.next
		prev_l.next = None
		return res

s = Solution()
l1 = ListNode(1,
		ListNode(1, 
			ListNode(2, None)))
l2 = ListNode(1,
		ListNode(1,
			ListNode(2,
				ListNode(3,
					ListNode(3, None)))))
res = s.deleteDuplicates(l1)
while res:
	print res.val
	res = res.next
