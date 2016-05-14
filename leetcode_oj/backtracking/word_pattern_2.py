'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Examples:
pattern = "abab", str = "redblueredblue" should return true.
pattern = "aaaa", str = "asdasdasdasd" should return true.
pattern = "aabb", str = "xyzabcxzyabc" should return false.
Notes:
You may assume both pattern and str contains only lowercase letters.

Hide Company Tags Dropbox Uber
Hide Tags Backtracking
Hide Similar Problems (E) Word Pattern

Difficulty: Hard
'''
class Solution(object):
    def wordPatternMatch(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

		'''
		Algorithm: 
		Here we don't have space between str char, so we
		don't know what pattern char can match in string
		count be 0.. n len string

		That reminds me backtracking.
		Base case: 
		if not pattern and not s: we're done
		if not pattern and s: we're done

		Else
		find ALL substring in s (DFS) that can match pattern
		and add into hash for next time
		'''
		return self.dfs(pattern, s, {}, {})


	def dfs(self, p, s, hash_p, hash_s):
		if not p and not s:
			return True
		if not p and s:
			return False

		# Starting with one as s[:0] is None
		# We can't match None.
		# Ending with len(s) - len(p).. its like we have
		# to match EACH char in Pattern with something in S
		for i in range(1, len(s) - len(p) + 1):
			if p[0] not in hash_p and s[:i] not in hash_s:
				hash_p[p[0]] = s[:i]
				hash_s[s[:i]] = p[0]
				#Find remaning
				match = self.dfs(p[1:], s[i:], hash_p, hash_s)
				if match:
					return True
				#we're here that means no more pattern is matching string
				del hash_p[p[0]]
				del hash_s[s[:i]]
			elif p[0] in hash_p and hash_p[p[0]] == s[:i] and hash_s[s[:i]] == p[0]:
				if self.dfs(p[1:], s[i:], hash_p, hash_s):
					return True
		return False
