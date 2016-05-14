'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
'''
class Solution(object):
	def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		s = "1"
		
		for i in range(1, n):
			last = s
			s = ""
			prev = last[0]; count = 1
			for j in range(1, len(last)):
				if prev == last[j]:
					count += 1
				else:
					s += str(count) + str(prev)
					prev = last[j]; count = 1
			s += str(count) + str(prev)

		return s
	
	def countAndSay2(self, n):
		import re
		s = "1"
		for i in range(1, n):
			counts, repeating = re.findall(r'((.)\2*)',s)[0]
			s = str(len(counts)) + str(repeating)	
		return s

s = Solution()
print s.countAndSay2(3)
