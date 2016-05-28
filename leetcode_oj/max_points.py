'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Hide Company Tags LinkedIn Apple Twitter
Hide Tags Hash Table Math
Difficulty: Hard
'''
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
        #key: slope, value, list of points
        #Point on same line: If slope same, or x-co-ordinate matches (means infinite slope)
        #Find max after eatch ith point
        h = {}
        max_global = 0
        for i in range(len(points)):
            p2 = points[i]
            h = {'i': 1} #Counting cur node
            same_points = 0
            for j in range(i+1, len(points)):
                p1 = points[j]
                #Same point:
                if p1.x == p2.x and p1.y == p2.y:
                    same_points += 1
                    continue
                delta_x = p2.x - p1.x 
                delta_y = p2.y - p1.y
                if delta_x == 0: #ON same line, with infinite slope
                    h['i'] += 1
                    continue
                m = float(delta_y)/(delta_x)
                try:
                    h[m]+=1 
                except:
                    h[m] = 2#Including ith point
                    
            max_cur_points = max(h.values()) + same_points
            max_global = max(max_global, max_cur_points)
                
        return max_global
        
    
