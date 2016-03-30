#!/usr/bin/python
class Solution:
    # @param num, a list of integers
    # @return a string
	def largestNumber(self, num):
		result = set()
		num_perm = self.find_permutation(num, result)
		print num_perm
		return max(result, key=lambda num: int(num))

	def find_permutation(self, list_num, num_perm):
		if len(list_num) == 1:
			return str(list_num[0])
		else:
			for i in range(0, len(list_num)):
				if i == 0:
					res = str(list_num[i]) + self.find_permutation(list_num[i+1:], num_perm)
					num_perm.add(res)
					res = self.find_permutation(list_num[i+1:], num_perm) + str(list_num[i])
					num_perm.add(res)
				else:
					res = str(list_num[i]) + self.find_permutation(list_num[:i] + list_num[i+1:], num_perm) 
					num_perm.add(res)
					res = str(self.find_permutation(list_num[:i] + list_num[i+1:], num_perm)) + str(list_num[i])
					num_perm.add(res)

s = Solution()
given = [3, 30, 34, 5, 9]
m = s.largestNumber(given)
print "Maximum: ", m
