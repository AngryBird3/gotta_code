'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
'''
from collections import deque
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
	def canFinish(self, numCourses, prerequisites):
		#q = deque()
		courses = {}
		#Construct graph: {node: incoming edge from}
		for i in range(len(prerequisites)):
			for j in range(1, len(prerequisites[i])):
				if prerequisites[j][i] not in courses:
					courses[prerequisites[j][i]] = list()
				courses[prerequisites[i][0]].append(prerequisites[i][j])
		
		print courses
		assert(len(courses) == numCourses)
		print p
		print visited
		return True

s = Solution()
#print s.canFinish(2, [[1,0]])
#print s.canFinish(2, [[1,0],[0,1]])
#print s.canFinish(3, [[1,2],[2,3]])
#print s.canFinish(4, [[1,2,6],[2,3],[3,6]])

#print s.canFinish(4, [[1,2],[2,3],[3,4],[4,2]])
print s.canFinish(6, [[1,6,7,8],[3,2],[2,1]])


