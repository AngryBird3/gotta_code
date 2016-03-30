'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
	def longestConsecutive(self, nums):
		h = {}
		m = 0
		for x in nums:
			h[x] = 1

		for x in nums:
			print "x: ", x
			#cl = self.helper_l(x,d)
			cl = 1
			if x in h:
				del h[x]
			a = x-1
			while True:
				if a not in h:
					#print "Break as ", a ," not there in h"
					break
				else:
					del h[a]
					cl += 1
					#print "a-1: ", a, h, " count: ", cl
					a -= 1
			b = x + 1
			cr = 0
			while 1:
				if b not in h:
					#print "Break as ", b, " not there in h"
					break
				else:
					del h[b]
					cr += 1
					#print "b: ", b, h, " count: ", cr
					b += 1
			#cr = self.helper_r(x+1,d)
			m = max(cl + cr, m)
		return m

	def helper_l(self, x, h, c=0):
		if x not in h:
			return c
		else:
			c += 1
			#del h[x-1]	
			r = dict(h)
			del r[x]
			print "x: ", x, r, " count: ", c
			return self.helper_l(x-1, r, c)

	def helper_r(self, x, h, c=0):
		if x not in h:
			return c
		else:
			c += 1
			#del h[x+1]
			l = dict(h)
			del l[x]
			print "x: ", x, l, " Right count: ", c
			return self.helper_r(x+1, l, c)

s = Solution()
print s.longestConsecutive([100, 4, 200, 1, 3, 2])
