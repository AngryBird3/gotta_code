'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Hide Company Tags Amazon Microsoft Bloomberg Uber
Hide Tags Hash Table Linked List
Hide Similar Problems (M) Clone Graph
Difficulty: Hard
'''
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        #key: node, value: copy_node
        h = collections.defaultdict(lambda: RandomListNode(0))
        h[None] = None
        n = head
        while head:
            h[head].label = head.label
            h[head].next = h[head.next]
            h[head].random = h[head.random]
            head = head.next
        return h[n]
