'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
Difficulty: Medium
 Microsoft Uber Facebook
Hide Tags Dynamic Programming String

'''
class Solution(object):
    def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0
		#opt[i] = # of ways to decode ..
		opt = [0 for i in range(len(s))]
		prev = int(s[0]) 
		opt[0] = 1 if prev > 0 else 0

		for i in range(1, len(opt)):
			cur = int(s[i])
			if cur > 0:
				opt[i] = opt[i-1] #Considering single digit convert (A-I or 1-9)
			print "i: ", i, " two digit: ", prev*10+cur
			num = prev * 10 + cur
			if (num < 27 and num > 9):
				if i > 1:
					opt[i] += opt[i-2] #Double digit convert, if # < 26 
				else:
					opt[i] += 1
			prev = cur
		return opt[i]

s = Solution()
print s.numDecodings("109")
