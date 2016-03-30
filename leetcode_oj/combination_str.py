'''
Print all the possible words combination from a long string  with no space.
'''
class Solution:
	def combination(self, s):
		self.res = list()
		self.helper(s, 0)
		return self.res

	def helper(self, s, start, temp=""):
		if temp:
			if temp not in self.res:
				self.res.append(temp)
		
		for i in range(start, len(s)):
			temp += s[i] 
			self.helper(s, i+1, temp)	
			temp = temp[:len(temp)-1]

s = Solution()
print s.combination("Dhara")
