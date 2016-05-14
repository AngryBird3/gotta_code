'''
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

Hint:

Consider the palindromes of odd vs even length. What difference do you notice?
Count the frequency of each character.
If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?
'''
class Solution(object):
	def canPermutePalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		h = {}
		for ch in s:
			if ch in h:
				h[ch] += 1
			else:
				h[ch] = 1
		
		num_of_even = 0
		num_of_odd = 0
		for ch in h:
			if h[ch] % 2 == 0:
				num_of_even += 1
			else:
				num_of_odd += 1
			if num_of_odd > 1:
				return False

		return True	

s = Solution()
print s.canPermutePalindrome("carerac")
