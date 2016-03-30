#!/usr/bin/python
'''
Given an input string, reverse the string word by word. 
A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing 
spaces and the words are always separated by a single space.
For example,
Given s = "the sky is blue",
return "blue is sky the".
Could you do it in-place without allocating extra space?
'''

class Solution:
	def revserse_words(self, s):
		if not s or len(s) == 1:
			return s
		#Idea:
		#	Reverse the whole string
		#	Now reverse in place all the words
		#	e.g. Dhara Darji
		#		- ijraD arahD
		#		- Darji	Dhara

		#Reverse the whole string
		w = list(s)
		self.reverse(w, 0, len(w)-1)

	 	#Reverse each word in place
		start = 0
		end = 0
		for i in range(0, len(w)):
			#Either its last work or space
			if w[i] == ' ' :
				self.reverse(w, start, i-1)
				start = i+1
		self.reverse(w, start, i)
		return ''.join(w)

	def reverse(self, w, start, end):
		i = start
		j = end
		while i < j:
			temp = w[i]
			w[i] = w[j]
			w[j] = temp
			i+=1
			j-=1
			
s = Solution()
a = "the sky is blue"
print "Reverse of ", a, "\nis: ", s.revserse_words(a)

