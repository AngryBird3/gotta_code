'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
import Queue
class Solution(object):
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		q = Queue.PriorityQueue()	

		for node in lists:
			if node:
				q.put((node.val, node))
	
		dummy = ListNode(0)
		while q.size() > 0:
			dummy.next = q.get()[1]#Get node
			dummy = dummy.next #We need to move to THAT node.
			#Add the next node to queue
			if dummy.next:
				q.put((dummy.next.val, dummy.next))	

		return dummy.next

s = Solution()
