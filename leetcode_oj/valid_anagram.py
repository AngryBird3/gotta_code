'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
'''
class Solution(object):
    def isAnagram(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		if not s and not t:
			return True
		if not s or not t:
			return False

		if len(s) != len(t):
			return False

		bit = [0 for i in range(256)]
		for i in range(len(s)):
			bit[ord(s[i])] += 1

		for j in range(len(t)):
			if bit[ord(t[j])] == 0:
				return False
			else:
				bit[ord(t[j])] -= 1

		return sum(bit) == 0

s = Solution()
print s.isAnagram("anagram", "nagaram")
