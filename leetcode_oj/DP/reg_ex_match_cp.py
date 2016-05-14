'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
Difficulty: Hard
 Google Uber Airbnb Facebook Twitter
Hide Tags Dynamic Programming Backtracking String
Hide Similar Problems (H) Wildcard Matching

'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p and s:
            return False
        ''' 
        opt[i][j] = True if s[..j] match p[...i]
        extra row and col: No Pattern or No Str
        '''
        rows = len(p) + 1 
        cols = len(s) + 1 
        opt = [[False for j in range(cols)] for i in range(rows)]
    
        opt[0][0] = True
        for i in range(1, rows):
            #if p[i-1] == '.':
            #   opt[i][0] = True
            if p[i-1] == '*':
                opt[i][0] = opt[i-1][0] or opt[i-2][0]

        for i in range(1, rows):
            for j in range(1, cols):
                #Case 1: when its not '*'
                if p[i-1] != '*':
                    opt[i][j] = opt[i-1][j-1] and (p[i-1] == s[j-1] or p[i-1] == '.')
                else:
					'''          * - 1            * - 0           * - +1 time, meaning without jth char it should be match too'''
                    opt[i][j] = (opt[i-1][j] or opt[i-2][j] ) or (opt[i][j-1] and (s[j-1] == p[i-2] or p[i-2] == '.'))

        return opt[-1][-1]

