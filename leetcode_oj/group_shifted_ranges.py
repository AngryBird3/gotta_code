'''
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''
import collections
class Solution(object):
	def groupStrings(self, strings):
		"""
		:type strings: List[str]
		:rtype: List[List[str]]
		"""
		res = list()
		if not strings:
			return res
		h = collections.defaultdict(list)
		#l = list()
		#for i in range(ord('a'), ord('z')+1):
		#	l.append(chr(i))	
		def key(s):
			return ''.join(map(lambda a: str((ord(a) - ord(s[0]))%26) + '-', s))

		for s in strings:
			h[key(s)].append(s)

		return map(sorted, h.values())

s = Solution()
strings = ["ef", "dd", "aa", "b", "aaa", "abc", "def"]
#strings = ["abc", "am"]
print s.groupStrings(strings)
