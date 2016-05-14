'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0 
        prev = cur = 0 
        rem = { 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1 } 
        for i in range(len(s) - 1, -1, -1):
            cur = rem[s[i]]
            if cur < prev:
                res -= cur 
            else:
                res += cur  
            prev = cur 
        return res
