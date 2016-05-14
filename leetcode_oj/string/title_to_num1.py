'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Hide Company Tags Microsoft Uber
Hide Tags Math
Hide Similar Problems (E) Excel Sheet Column Title
Difficulty: Easy
'''
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        num = 0 
        for i in xrange(0, len(s)):
            num =  num * 26 + (ord(s[i]) % 64)
        return num  


