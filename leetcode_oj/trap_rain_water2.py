class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        Find MAX height in the given heights
        which would serve as Boundry (left/right) for 'bucket'
        
        Left to MAX_HEIGHT:
        DO one of thise things
        -- Find leftmost boudry height - left_heighest
        -- water += left_heighest - height[i]
        
        From right to MAX_HEIGHT
        do same!
        '''
        
        max_height = -1; max_height_index = -1
        for i in range(len(height)):
            if max_height < height[i]:
                max_height = height[i]
                max_height_index = i
                
        # Now lets calculate water from both the end
        water = 0
        # Left to max_height_index
        # which is serving as right most boundry
        boundry = -1 #left boundry
        for i in range(0, max_height_index):
            if height[i] > boundry:
                boundry = height[i]
            else:
                water += (boundry - height[i])
                
        # Right to max_height_index
        # which is serving as left most boundry
        boundry = -1#Right boundry
        for i in range(len(height)-1, max_height_index, -1):
            if height[i] > boundry:
                boundry = height[i]
            else:
                water += (boundry - height[i])
                
        return water
