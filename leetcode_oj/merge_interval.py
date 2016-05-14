'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
 LinkedIn Google Facebook Twitter Microsoft Bloomberg Yelp
Hide Tags Array Sort
Hide Similar Problems (H) Insert Interval (E) Meeting Rooms (M) Meeting Rooms II
Difficulty: Hard
'''
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
	def merge(self, intervals):
		#sort with start time
		intervals = sorted(intervals, key = lambda s: s.start)

		j = 0
		res = list()
		res.append(intervals[0])
		for i in range(1, len(intervals)):
			#prev.end > cur.start then prev.end = cur.start
			if res[j].end >= intervals[i].start:
				res[j].end = max(res[j].end, intervals[i].end)
			else:
				res.append(intervals[i])
				j+=1
		return res
	def print_i(self, res):
		for i in res:
			print "[",i.start, ", ", i.end, "]",

s = Solution()
l = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
res = s.merge(l)
s.print_i(res)
