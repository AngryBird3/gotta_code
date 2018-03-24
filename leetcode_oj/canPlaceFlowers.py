'''
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
'''
class Solution(object):
	def canPlaceFlowers(self, flowerbed, n):
		"""
		:type flowerbed: List[int]
		:type n: int
		:rtype: bool
		"""
		c = 0
		for i in range(0, len(flowerbed)):
			if not flowerbed[i] and (i < 1 or not flowerbed[i - 1]) and (i == len(flowerbed) - 1 or not flowerbed[i + 1]):
				flowerbed[i] = 1
				c += 1
				if c >= n:
					return True
		return c >= n

s = Solution()
print s.canPlaceFlowers([0,0,1,0,0], 1)
