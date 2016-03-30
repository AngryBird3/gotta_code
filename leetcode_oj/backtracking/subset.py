'''
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
	def subsets(self, nums):
		result = list()
		nums.sort()
		print nums
		self.find_subsets(nums, list(), result)
		return result
	
	def find_subsets(self, rest, so_far, result):
		if not rest:
			if so_far not in result:
				result.insert(0, so_far)
		else:
			self.find_subsets(rest[1:], so_far + [rest[0]], result)
			self.find_subsets(rest[1:], so_far, result)

s = Solution()
print s.subsets([1,2,3])
