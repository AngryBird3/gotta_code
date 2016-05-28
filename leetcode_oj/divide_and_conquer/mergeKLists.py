'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Hide Company Tags LinkedIn Google Uber Airbnb Facebook Twitter Amazon Microsoft
Hide Tags Divide and Conquer Linked List Heap
Hide Similar Problems (E) Merge Two Sorted Lists (M) Ugly Number II
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        k = len(lists)
        if k == 0:
            return lists
        elif k == 1:
            return lists[0] 
        else:
            d = k/2
            return self.merge2lists(self.mergeKLists(lists[:d]), self.mergeKLists(lists[d:]))        

    def merge2lists(self, l1, l2):
        l = ListNode(None)
        head = l 
        while l1 and l2: 
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next
        l.next = l1 or l2

        return head.next   

