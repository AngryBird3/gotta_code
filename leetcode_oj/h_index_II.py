'''
A scientist has index h if h of his/her N papers have at least h citations each, and the other N - h papers have no more than h citations each.
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
https://leetcode.com/problems/h-index-ii/
'''
class Solution(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		start = 0
		n = len(citations)
		end = n-1
		highest = 0
		while start <= end:
			mid = (start + end)/2
			#print "start: ", start, " end: ", end
			#print "citations[mid]: ", citations[mid], "n - mid: ", n-mid
			if citations[mid] == (n - mid):
				return citations[mid]
			if citations[mid] < (n - mid):
				start = mid + 1 
			else:
				end = mid - 1
			#	highest = 

		#print "Not found"
		#print "start: ", start
		return n-(start)

s = Solution()
print s.hIndex([0,1,])
