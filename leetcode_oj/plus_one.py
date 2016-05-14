'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [0]
        n = len(digits) - 1
        res = list()
        c = digits[n] + 1
        res.append(c%10)
        c = c/10
        for i in range(n-1, -1, -1):
            print i
            if c == 0:
                res = digits[:i+1] + res
                break
            c = digits[i] + c
            res.insert(0, c%10)
            c = c/10
        if c:
            res.insert(0, c)
        return res
