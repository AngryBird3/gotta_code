'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
 Dropbox Google Uber Snapchat Twitter
Hide Tags Dynamic Programming Backtracking

Difficulty: Hard
'''
class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: Set[str]
		:rtype: List[str]
		"""

		'''
		Algorithm:
		1) Find out if we can really split given string (similar to word-break1)
		2) If so get the solution with backtracking from dp matrix
		'''
		# opt[i] is true if we can split string[0...i]
		opt = [0] * (len(s) + 1)
		if not self.can_break(s, wordDict, opt):
			return list()

		res = self.split_string(s, len(s), wordDict, opt)
		return res
	
	def can_break(self, s, wordDict, opt):
		''' for opt[i], we can if [0..i] in dict or can be split, then true '''
		for i in range(len(s) + 1):
			if s[:i] in wordDict:
				opt[i] = True
				#print "i: ", i , " s[:i]: " , s[:i]
			else:
				#print " else i: ", i 
				for j in range(0, i + 1):
					#print "		j: ", j , " s[j:i]: " , s[j:i]
					opt[i] = opt[i] or (opt[j] and s[j:i] in wordDict)
		print opt
		return opt[-1]

	def split_string(self, s, end, wordDict, opt):
		''' Return resultant split from s[0] .. s[end] '''
		res = list()
		for i in range(0, end):
			if opt[i] and s[i:end] in wordDict:
				remaining_res = self.split_string(s, i, wordDict, opt)
				for strs in remaining_res:
					res.append(strs + " " + s[i:end])
		if s[0:end] in wordDict:
			res.append(s[0:end])
		return res

s = Solution()
print s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])	
