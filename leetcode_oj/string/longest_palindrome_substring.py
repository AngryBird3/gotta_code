'''
Find UNIQ longest common substring
Remember Uniq, longest word doesnt matter!
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''
class Solution:
	def lps(self, s):
		if not s:
			return None

		if len(s) == 1:
			return s

		"abbacdcfcc"
		"cccdcabba"
		"aba"
		"aa"
		start = 0
		m = 1

		for i in range(1, len(s)):
			if (i-m-1) >= 0 and s[i-m-1:i+1] == s[i-m-1:i+1][::-1]:
				start = i-m-1
				m += 2
			elif (i-m) >=0 and s[i-m:i+1] == s[i-m:i+1][::-1]:
				start = i - m
				m += 1
			print "i: ", i, "at char: ", s[i], " max: ", m, " pal: ", s[start:start+m] 
		return s[start:start+m]
s = Solution()
print s.lps("abbacdcfcc")
#print s.lps("cccdcabba")
#print s.lps("xyzabba1abba")
