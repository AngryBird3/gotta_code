'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
	def combine(self, n, k):
		self.res = list()
		self.helper(0, n, k)
		return self.res

	def helper(self,start, n, k, temp=list()):
		if len(temp) == k:
			print temp
			self.res.append(temp[:])
			return

		for i in range(start, n):
			temp.append(i+1)
			#print "i+1: ", i+1, " start: ", start, " temp: ", temp
			self.helper(i+1, n, k, temp)
			temp.pop()

s = Solution()
print s.combine(3, 2)
