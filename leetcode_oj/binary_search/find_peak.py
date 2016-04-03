'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''
class Solution:
    # @param nums, an integer[]
    # @return an integer
	def findPeakElement(self, nums):
		p = self.findPeakRec(nums, 0, len(nums))
		return p
	
	def findPeakRec(self, nums, start, end):
		mid = (end + start)/2
		n = len(nums) - 1
		if (mid == 0 or nums[mid - 1] <= nums[mid]) and (mid == n or  nums[mid + 1] <= nums[mid]):
			return mid;
		elif (mid > 0 and nums[mid - 1] > nums[mid]):
			#Peak is on left:
			return self.findPeakRec(nums, start, mid)
		else:
			#Peak is on right:
			return self.findPeakRec(nums, mid + 1, end)
s = Solution()
a = [1, 2, 3, 1]
#a = [1,1,1]
#a = [1]
#a = [3, 1, 1]
#a = [1, 2, 3]
print s.findPeakElement(a)
