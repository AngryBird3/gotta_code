'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
'''
from heapq import heappush, heappop
#Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
	def minMeetingRooms(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: int
		"""
		'''
		Algorithm:
			- Sort the intervals with start time
			- Keep heap(min heap) with end time ( which is room's meeting end time)
			- Consider heap/room as bucket
			- When can I add an interval into my bucket:
				- If cur_iternval.start > room.end:
					sure go ahead, use same room
			- Why heap? Minheap will give me a room which has earliest 
			  end time
		'''
		h = []
		intervals = sorted(intervals, key=lambda x: x[0])
		heappush(h, intervals[0][1])
		room = 1
		for i in range(1, len(intervals)):
			if intervals[i][0] >= h[0]:
				heappop(h)
				heappush(h, intervals[i][1])
			else:
				print "room end: ", h[0]
				print "intervals[",i, "][0]: ", intervals[i][0]
				room += 1
				heappush(h, intervals[i][1])
		return room
s = Solution()
print s.minMeetingRooms([[0, 30],[5, 10],[15, 20]])
#print s.minMeetingRooms([[3, 7], [7, 20]])
#print s.minMeetingRooms([[2, 11], [11, 16], [6, 16]])
