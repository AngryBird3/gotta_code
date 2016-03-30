'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
	def findKthLargest(self, nums, k):
		l = 0
		r = len(nums) - 1
		k -= 1
		while(True):
			pivot = (r + l)/2
			print "pitvot: ", pivot
			pos = self.partition(nums, l, r, pivot)
			print "pos: ", pos
			if (pos == k):
				return nums[pos];
			elif pos < k:
				l = pos + 1
			else:
				r = pos - 1
			print "l: ", l, "r: ", r, "k: ", k
	def partition(self, nums, l, r, pivot):
		x = nums[pivot]
		self.swap(nums, pivot, r)
		j = l
		for i in range(l, r):
			if nums[i] > x:	
				self.swap(nums, i, j)
				j += 1
		self.swap(nums, j, r)
		return j
	
	def swap(self, nums, a, b):
		temp = nums[a]
		nums[a] = nums[b]
		nums[b] = temp

s = Solution()
a = [3,2,1,5,6,4]
print s.findKthLargest(a, 1)
