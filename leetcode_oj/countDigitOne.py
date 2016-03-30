'''
Given an integer n, count the total number of digit 1 appearing in all 
non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
'''
class Solution:
    # @param {integer} n
    # @return {integer}
	def countDigitOne(self, n):
		base = 1; last = 0; res = 0; i = 0

		while n >= base:
			i += 1
			print "\nIteration: ", i
			index = (n / base) % 10
			remain = n - (n / base) * base;
			if index > 1:
				res = res + index * last + base
			elif index == 1:
				res = res + index * last + remain + 1
			else:
				res = res + index * last
			last = last * 10 + base
			base = base * 10
			print "Res: ", res
			print "Index: ", index, " Remain: ", remain
			print "Last: ", last, " Base: ", base
		print "....\n"
		return res

s = Solution()
print s.countDigitOne(21)
