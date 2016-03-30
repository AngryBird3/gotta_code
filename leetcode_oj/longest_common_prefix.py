#Write a function to find the longest common prefix string amongst an array of strings.
class Solution:
    # @param {string[]} strs
    # @return {string}
	def longestCommonPrefix(self, strs):
		if len(strs) < 1:
			return ""
		if len(strs) == 1:
			return strs[1]
		'''
		for i in range(0, len(strs[0])):
			c = strs[0][i]
			for j in range(1, len(strs)):
				#print strs[j]
				if i >= len(strs[j]) or strs[j][i] != c:
					break
				if j == len(strs):		
					return strs[j][0: i]
				else:
					return ""
		'''

		for j in xrange(0, len(strs[0])):
			print "j: ",j
			for i in xrange(0,len(strs)-1):
				print "i: ", i
				print "strs[i+1]: ", strs[i+1]
				print "strs[i]: ", strs[i]
				if (j >= len(strs[i+1]) or strs[i][j]!=strs[i+1][j]):
					if j==0:
						return ""
					else:
						print "Ans: strs[i][0:j]: i -", i, "j: ", j
						return strs[i][0:j]

		return strs[0]
			
s = Solution()
#a = ["shash","shank","shashank","sha"]
a = ["defg" , "def", "defgh","de"];
print s.longestCommonPrefix(a)
