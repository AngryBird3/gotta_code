'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

Hide Company Tags Facebook
Hide Tags Math String
Hide Similar Problems (M) Add Two Numbers (M) Multiply Strings (E) Plus One
Difficulty: Easy
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = ""
        c = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or c:
            a1 = int(a[i]) if i >= 0 else 0
            b1 = int(b[j]) if j >= 0 else 0
            c = a1 + b1 + c
            s = str(c%2) + s
            c = c / 2
            i -= 1
            j -= 1
        return s
