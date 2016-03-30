'''
Given a stream of numbers, write code to 
calculate the rolling average and rolling 
max over two different window sizes

e.g. 
[1,2,3,4,5,6]
the following tuples would be expected,
where None indicates that a value is
not available
[None, None, None, None]
[None, None, None, None]
[2, 3, None, None]
[3, 4, None, None]
[4, 5, 3, 5]
[5, 6, 4, 6]


I'm solving for one window
Writing generator to yield (avg, max)
'''
from collections import deque
class Solution:
	def sliding_window_avg_max(self, nums, w=3):
		d = deque(maxlen = w)	
		total = 0
		for n in nums:
			if len(d) >= w:
				total = total - d.pop() + n 
			else:
				total = total + n
			d.append(n)
			if len(d) >= w:
				yield (total/float(w), max(d))	
			else:
				yield(None, None)

s = Solution()
a = [1, 2, 3, 4, 5, 6]
for t in s.sliding_window_avg_max(a):
	print t 
