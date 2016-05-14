class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(-1)
        head = res
        c = 0
        while l1 or l2 or c:
            c += l1.val if l1 else 0
            c += l2.val if l2 else 0
            res.next = ListNode(c % 10)
            c = c / 10
            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return head.next
