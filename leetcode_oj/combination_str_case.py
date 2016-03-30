'''
Write code to generate all possible case combinations of a given lower-cased string. (e.g. "0ab" -&gt; ["0ab", "0aB", "0Ab", "0AB"])
'''

class Solution:
	def combination(self, s):
		self.res = list()
		self.helper(0, s)

		return self.res

	def helper(self, idx, s, temp = ""):
		if len(temp) == len(s):
			self.res.append(temp[:])
			print temp

		if idx > len(s)-1:
			return
		if s[idx].islower():
			self.helper(idx+1, s, temp + s[idx].upper())
		self.helper(idx + 1, s, temp + s[idx]) 

s = Solution()
print s.combination("0ab")
