'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

Hide Tags
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        """
        323

        32 3
        3   32
        
        3223
        
        322 3
        32   32
        """
        if x <0 or (x and x%10 == 0):
            return False
        rev = 0
        while x > rev:
            rev = rev* 10 + (x%10)
            x /= 10
        return x == rev or x == rev/10
