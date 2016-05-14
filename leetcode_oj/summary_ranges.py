'''
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
 Google
Hide Tags Array
Hide Similar Problems (M) Missing Ranges
Difficulty: Medium
'''
class Solution(object):
	def summaryRanges(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		if not nums:
			return list()
		res = list()
		start = nums[0]
		end = None
		for i in range(1, len(nums)):
			if nums[i] != nums[i-1] + 1:
				end = nums[i-1]
				if start != end:
					res.append(str(start) + "->" + str(end))
				else:
					res.append(str(start))
				start = nums[i]
			else:
				end = nums[i]
		if not end or start >= end:
			res.append(str(start)) 
		else:
			res.append(str(start) + "->" + str(end))
		#if not end and start <= nums[i]:
		#	res.append(str(start) + "->" + str(nums[i]))
		return res

s = Solution()
print s.summaryRanges([1, 3])
