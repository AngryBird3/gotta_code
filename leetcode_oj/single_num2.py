class Solution:
    # @param {integer[]} nums
    # @return {integer}
	def singleNumber(self, nums):
		ones = 0
		twos = 0

		for x in nums:
			twos = twos | (ones & x)
			ones = ones ^ x 
			common_bit_mask = ~(ones & twos)
			ones = ones & common_bit_mask
			twos = twos & common_bit_mask
			print "x: ", x, "ones: ", ones, "twos: ", twos, "common_bit_mask: ", common_bit_mask

		return ones

s = Solution()
#a = [3,3,2,3]
a = [4,3,8,4,8,4,8]
print s.singleNumber(a)
