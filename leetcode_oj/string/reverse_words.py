'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
		return "".join(s.split()[::-1])

	def reverseWords2(self, s):
		s[::-1]
        start = 0
        for i in range(len(s)):
            if s[i].isspace():
                self.reverse(s, start, i-1)
                start = i+1
        self.reverse(s, start, len(s)-1)
        
    	def reverse(self, s, start, end):
        	while start < end:
            	temp = s[start]
            	s[i] = s[end]
            	s[end] = temp
            	start += 1
            	end -= 1
            
