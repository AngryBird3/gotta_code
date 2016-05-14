'''
Find all possible unique palindromes of size greater than 1 for a string.
'''

def all_palindromes(s):
	'''
	Algorithm:
	- start with one char, and grow on both the side to see if it matches
	  if so add to palidrome list
	- This we have to do for 1 .. n char in given s
	- Also for each char we have two choice:
		- Odd length palindrome: Grows by +2
		- Even length palindrome: Grows by +1
	'''

	res = set()
	for i in range(len(s)):

		#Odd length
		start = i-1
		end = i+1
		while start >= 0 and end < len(s) and s[start] == s[end]:
			res.add(s[start:end+1])
			start -= 1
			end += 1

		#Even length
		start = i
		end = i+1
		while start >= 0 and end < len(s) and s[start] == s[end]:
			res.add(s[start:end+1])
			start -= 1
			end += 1

	return list(res)

print all_palindromes("abbacdcfcc")
