'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        # Push openning brackets into stack
        # Pop from stack when close brackets
        # come, and match with pop'ed one
        stack = list()
        h = {"{":"}", "(":")", "[": "]"}
        open_p = {"{": 1, "[":1, "(": 1}
        closing_p = {"}":1, "]":1, ")":1}
        for b in s:
            if b in open_p:
                stack.append(b)
            elif b in closing_p:
                if not stack or h[stack.pop()] != b:
                    return False
        return True if not stack else False 
