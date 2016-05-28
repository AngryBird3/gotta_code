'''
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
Microsoft Google Facebook Twitter Yelp
Hide Tags Binary Indexed Tree Segment Tree Heap Divide and Conquer
'''
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = set([b[0] for b in buildings] + [b[1] for b in buildings])
        live_buildings = []
        res = list()
        i = 0
        for p in sorted(points):
            #print "p: ", p, " live_buildings: ", live_buildings
            #Add into heap, if the buildings left <= current point p
            while i < len(buildings) and buildings[i][0] <= p:
                #print "building (left): ", buildings[i][0]
                heapq.heappush(live_buildings, (-buildings[i][2], buildings[i][1]))
                i += 1
                
            #Pop "non" live buildings, as in which right is < cur p
            while live_buildings and live_buildings[0][1] <= p:
                #print "removing non live building (right): ", live_buildings[0][1]
                heapq.heappop(live_buildings)
                
            #Now its the time to add max_height point into results
            #x = p, height = max_height from livebuilding
            h = -live_buildings[0][0] if live_buildings else 0
            #Ok we can't just add directly, cause we need left most point of a line
            #i.e. if we've already added a point with h height, then ignore!
            if not res or h != res[-1][1]:
                #print "Adding p: ", p , " h: ", h
                res.append((p, h))
        return res
