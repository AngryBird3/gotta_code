'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
 Google Uber Zenefits
Hide Tags Backtracking String
Hide Similar Problems (M) Letter Combinations of a Phone Number (E) Valid Parentheses

Difficulty: Medium
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return list()
        self.res = list()
        num_open = 0 
        num_close = 0 
        s = ""
        self.helper(n, s, num_open, num_close)
        return self.res

    def helper(self, n, s, o, c): 
        if c == n:
            self.res.append(s)
        else:
            if o < n:
                self.helper(n, s+"(", o+1, c)
            if c < o:
                self.helper(n, s+")", o, c+1)
