'''
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a")  false
isMatch("aa","aa")  true
isMatch("aaa","aa")  false
isMatch("aa", "*")  true
isMatch("aa", "a*")  true
isMatch("ab", "?*")  true
isMatch("aab", "c*a*b")  false
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
		opt[i][j] = True if s[..j] match p[..i]
		extra row nd col: No pattern and No string
		'''
		rows = len(p) + 1
		cols = len(s) + 1
		opt = [[False for j in range(cols)] for i in range(rows)]

		opt[0][0] = True

		# 0 length string but we've pattern
		# if prev's pattern true and current is * (as * can eliminate everything) or ?
	
		for i in range(1, rows):
			opt[i][0] = opt[i-1][0] and (p[i-1] == "*" or p[i-1] == "?")

		for i in range(1, rows):
			for j in range(1, cols):
				#1) If its NOT *; easy one - update diagonally; if current is same or ? =? true 
				if p[i-1] != "*":
					opt[i][j] = opt[i-1][j-1] and (p[i-1] == s[j-1] or p[i-1] == "?")
				else:
					#2) If its *, i-1 and j match, vertical [i-1][j] or horizontal [i][j-1]
					opt[i][j] = opt[i-1][j] or opt[i][j-1]
		return opt[-1][-1]

s = Solution()
print s.isMatch("aab", "c*a*b")
