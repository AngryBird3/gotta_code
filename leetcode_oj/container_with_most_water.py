'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        '''
        Algorithm:
        Lines looks like this:
    
              |
          |   |      |
        | |   | |    |
        |_|_|_|_|_|__|
        
        We want to maximize length * width
        we start with leftmost and right most lines.
        
        IF the left line is shorter than the right
        we move left(we dont need to compute area
        for left and rightmostline - 1 as its gonna
        be shorter and smaller length)
        '''
        low = 0
        high = len(height)-1
        maxarea = 0
        while low < high:
            maxarea = max(maxarea, (high - low) * min(height[low], height[high]))
            #print "high: ", high, " low: ", low, "height_low: ", height[low], " height_high: ", height[high]
            #print "maxarea: ", maxarea
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return maxarea
