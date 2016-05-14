'''
Given a column title as appear in an Excel sheet, return its 
corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
'''

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
		pos = {}
		pos['A'] = 1
		for i in range (1, 27):
			pos[chr(ord('A')+i)] = i+1
		if len(s) == 1:
			return pos[s]
		num = 0
		for i in range(0, len(s)):
			num =  num * 26 + pos[s[i]] 
		return num
    def numberToTitle(self, n):
		pos = {}
		pos[0] = "Z" 
		pos[1] = "A"
		for i in range (2, 26):
			pos[i] = chr(ord('A')+i-1)
		t = ""
		while(n):
			r = n % 26
			t += pos[r]
			if r != 0:
				n /= 26
			else:
				n = n/26 - 1
		return t[::-1]

s = Solution()
print s.titleToNumber('AZ')
print s.numberToTitle(51)
