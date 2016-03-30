# Definition for singly-linked list.
class ListNode:
     def __init__(self, x, node):
         self.val = x
         self.next = node

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
		if headA == None or headB == None:
			return None

		if headA.next and headA.next.val == headB.val:
			return headB
		
		if headB.next and headB.next.val == headA.val:
			return headA

		
		da = 0
		current = headA
		while(current != None):
			da+=1
			current = current.next

		db = 0
		current = headB
		while(current != None):
			db+=1
			current = current.next

		d = abs(da - db)
		current = headA
		another = headB

		if db > da:
			current = headB
			another = headA
		while(d):
			current = current.next
			d-=1
		
		while(current != None or another != None):
			if (current.val == another.val):
				print "Intersection at: ", current.val
				return current
			current = current.next
			another = another.next

		return None		

c3 = ListNode("c3", None)
c2 = ListNode("c2", c3)
c1 = ListNode("c1", c2)
a2 = ListNode("a2", c1)
a1 = ListNode("a1", a2)
b3 = ListNode("b3", c1)
b2 = ListNode("b2", b3)
b1 = ListNode("b1", b2)

s = Solution()
inter = s.getIntersectionNode(a1, b1)
