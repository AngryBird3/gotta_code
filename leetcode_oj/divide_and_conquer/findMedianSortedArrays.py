'''
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
'''
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
	def findMedianSortedArrays(self, nums1, nums2):
		l = len(nums1) + len(nums2)
		if l%2 != 0:
			return self.kth(nums1, nums2, l//2)
		else:
			return (self.kth(nums1, nums2, l//2) + self.kth(nums1, nums2, l//2 - 1))/2.0

	def kth(self, a, b, k):
		if not a:
			return b[k]
		if not b:
			return a[k]
		ai = len(a)//2
		bi = len(b)//2

		ma = a[ai]
		mb = b[bi]

		# when k is bigger than the sum of a and b's median indices 
		if ai + bi < k:
			if ma > mb:
				# if a's median is bigger than b's, b's first half doesn't include k
				return self.kth(a, b[bi + 1: ], k - bi - 1)
			else:
				return self.kth(a[ai + 1: ], b, k - ai - 1)
		# when k is smaller than the sum of a and b's median indices 
		else:
			if ma > mb:
				return self.kth(a[:ai], b, k)
			else:
				return self.kth(a, b[:bi], k)

s = Solution()
a = [2, 6, 8, 9, 11, 12]
b = [1, 3, 5, 7, 10]
print s.findMedianSortedArrays([], [2, 3]) 
