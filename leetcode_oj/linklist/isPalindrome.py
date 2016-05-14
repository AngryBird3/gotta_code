'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

Hide Company Tags Amazon Facebook
Hide Tags Linked List Two Pointers
Hide Similar Problems (E) Palindrome Number (E) Valid Palindrome (E) Reverse Linked List
Difficulty: Easy
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = rev 
            rev = slow
            slow = slow.next
            rev.next = tmp 
        if fast:
            slow = slow.next

        head = slow
        tmp = None
        tail = rev 
        ispal = True
        while slow and rev:
            if slow.val != rev.val:
                ispal = False
            slow = slow.next
            cur = rev 
            rev = rev.next
            cur.next = tmp 
            tmp = cur 
    
        #Joining two halfs
        if tail:
            tail.next = head
        return ispal

