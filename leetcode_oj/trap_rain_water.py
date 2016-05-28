'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Hide Company Tags Google Twitter Zenefits Amazon Apple Bloomberg
Hide Tags Array Stack Two Pointers
Hide Similar Problems (M) Container With Most Water (M) Product of Array Except Self
'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        For ith height, we need to find a height which is greater than or equal to ith
        or end of the array (find a |_|- u shape)

		Max water would be left - right * min(height(left), height(right))
		But we can have internally u shapes holes!

		so with two pointer, left and right, fix max height pointer
		and let water flow/fill in from lower side

		Why MAX height?
		Its like border of our bin U. if its
		current is lower than max, water can fill on TOP
		of it, within border
        """
        if not height:
            return 0
        start = 0
        end = len(height) - 1
        maxHeightLeft = height[start]
        maxHeightRight = height[end]
        ret = 0
        while start < end:
            maxHeightLeft = max(height[start], maxHeightLeft)
            maxHeightRight = max(height[end], maxHeightRight)

            if maxHeightLeft < maxHeightRight:
                ret += maxHeightLeft - height[start]
                start += 1
            else:
                ret += maxHeightRight - height[end]
                end -= 1
        return ret
