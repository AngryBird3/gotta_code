'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.

Hide Tags Array Stack
Hide Similar Problems (H) Maximal Rectangle
Difficulty: Hard
'''
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        #Keep mix-stack, which has following property
        #Bottom-most element is with smallest height and going
        #top increases its height

        """
        The HUGE gotcha is:
        first thing on stack is -1.
        It helps when we're couting for 'last'
        element just before -1. We can get width with previous element
        as it is gonna be greater than the first stack

        consider: 4,2,4
        """
        heights.append(0)#Last border
        stack = list()
        stack.append(-1)#first border, this will stay forever 
        max_area = 0
        i = 0
        for i in range(len(heights)):
            #If current height is less than top of stack
            #that is going to serve as right boundry
            #pop all the entries till cur is > stack top
            print "h[i]: ", heights[i], " stack: ", stack
            while stack and heights[i] < heights[stack[-1]]:
                #Calculate area, top as new min height
                h = heights[stack[-1]]
                w = i - stack[-1] - 1#Right - previous - 1; i is right most border
                print "i: ", i, " stack[-1]: ", stack[-1], " stack: ", stack, " w: ", w, " h: ", h
                stack.pop()
                max_area = max(max_area, h * w)
            stack.append(i)

        return max_area

s = Solution()
h = [1,2,1]
print s.largestRectangleArea(h)
