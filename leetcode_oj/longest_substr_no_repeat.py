'''
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
'''
class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0
		c_start, c_end = 0, 0
		c_hash ={}

		c_hash[s[0]] = 0
		maxl = 1
		for i in range(1, len(s)):
			# IF we encounter a letter which already exists
			# in c_hash, save cur len, move start to exists_letter_index + 1
			# Of course only if that existing letter index > start (in current
			# substring
			if s[i] in c_hash and c_hash[s[i]] >= c_start:
				print "changing start at i: ", i
				c_start = c_hash[s[i]] + 1
			else:
				maxl = max(maxl, i - c_start + 1)
				print "i: ", s[i], " maxm: ", maxl
			c_hash[s[i]] = i
		return maxl

s = Solution()
print s.lengthOfLongestSubstring("vqblqcb")
