'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a")  false
isMatch("aa","aa")  true
isMatch("aaa","aa")  false
isMatch("aa", "a*")  true
isMatch("aa", ".*")  true
isMatch("ab", ".*")  true
isMatch("aab", "c*a*b")  true
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
		opt[i][j] = True if s[..j-1] match p[...i-1]
		extra row and col: No Pattern or No Str
		'''
		rows = len(p) + 1
		cols = len(s) + 1
		opt = [[False for j in range(cols)] for i in range(rows)]
		
		opt[0][0] = True
		for i in range(1, rows):
			#if p[i-1] == '.':
			#	opt[i][0] = True
			if p[i-1] == '*':
				opt[i][0] = opt[i-1][0] or opt[i-2][0]

		for i in range(1, rows):
			for j in range(1, cols):
				#Case 1: when its not '*'
				if p[i-1] != '*':
					opt[i][j] = opt[i-1][j-1] and (p[i-1] == s[j-1] or p[i-1] == '.')
				else:
					'''or opt[i-2][j]'''
					# Why opt[i-2][j]: Consider ab*c* and string: abbb: Then at last * - we consider prev pattern 0 (meaning till i-2)
					#opt[i][j] = (opt[i-1][j] or opt[i-2][j] ) or (opt[i][j-1] and (s[j-1] == p[i-2] or (p[i-2] == '.'and s[j-1] == s[j-2])))
					opt[i][j] = (opt[i-1][j] or opt[i-2][j] ) or (opt[i][j-1] and (s[j-1] == p[i-2] or p[i-2] == '.'))
				'''
				if i == 3 and j == 2:
					print "opt[3][2]: ", opt[3][2]	
				if i == 2 and j == 2:
					print "opt[2][2]: ", opt[2][2]
				if i == 1 and j == 2:
					print "opt[1][1]: ", opt[1][1] 
				'''

		return opt[-1][-1]
s = Solution()
print s.isMatch("aa","a")  
print s.isMatch("aa","aa") 
print s.isMatch("aaa","aa")
print s.isMatch("aa", "a*")
print s.isMatch("aa", ".*")
print s.isMatch("ab", ".*")
print s.isMatch("aab", "c*a*b")
