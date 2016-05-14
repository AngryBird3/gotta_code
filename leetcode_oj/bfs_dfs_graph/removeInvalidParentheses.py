'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
Credits:
Special thanks to @hpplayer for adding this problem and creating all test cases.

Hide Company Tags Facebook
Hide Tags Depth-first Search Breadth-first Search
Hide Similar Problems (E) Valid Parentheses
Difficulty: Hard
'''
from collections import deque
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def valid_parentheses(s):
            count = 0
            for a in s:
                if a == "(":
                    count += 1
                elif a == ")":
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        if not s:
            return [""]

        q = deque()
        res = list()
        if not valid_parentheses(s):
            q.append(s)
        else:
            res.append(s)
        visited = set()
        #Do BFS
        done = False
        while q:
            invalid_s = q.popleft()
            #Removed one char add into q
            if valid_parentheses(invalid_s):
                res.append(invalid_s)
                done = True
            if done:
                continue
            else:
                for i in range(len(invalid_s)):
                    if invalid_s[i] == "(" or invalid_s[i] == ")":
                        next_level = invalid_s[:i] + invalid_s[i+1:]
                        if next_level not in visited:
                            q.append(next_level)
                            visited.add(next_level)
        if not res:
            return [""]
        return res
