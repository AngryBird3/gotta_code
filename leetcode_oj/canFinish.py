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
		visited = {}
		#q = deque()
		courses = {}
		p = list()
		for i in range(len(prerequisites)):
			p.append(prerequisites[i][0])
			if prerequisites[i][0] not in courses:
				courses[prerequisites[i][0]] = list()
				visited[prerequisites[i][0]] = False
			for j in range(1, len(prerequisites[i])):
				if prerequisites[i][j] not in courses:
					courses[prerequisites[i][j]] = list()
					visited[prerequisites[i][j]] = False
				courses[prerequisites[i][0]].append(prerequisites[i][j])
		
		print courses
		assert(len(courses) == numCourses)
		print p
		print visited
		for c in p:
			#print "Looking for node: ", c
			if not visited[c]:
				if self.isCyclic(c, courses, visited, -1):
					return False

		return True

	def isCyclic(self, v, courses, visited, parent):
		# Mark current node visited
		visited[v] = True
		print "visited: ", visited, " node: ", v, " parent: ", parent

		#Recur for all the vertices adjacent to this vertex
		for adj in courses[v]:
			#If an adjacent is not visited, then recur for that adjacent	
			if not visited[adj]:
				if self.isCyclic(adj, courses, visited, v):
					return True
				else:
					return False
			#If an adjacent is visited and not parent of current vertex,
			#then there is a cycle.
			#elif adj != parent:
				#print "parent: ", parent, " adj: ", adj, " v: ", v
			else:
				return True
		#print "Returning False for node: ", v
		return False
s = Solution()
#print s.canFinish(2, [[1,0]])
#print s.canFinish(2, [[1,0],[0,1]])
#print s.canFinish(3, [[1,2],[2,3]])
#print s.canFinish(4, [[1,2,6],[2,3],[3,6]])

#print s.canFinish(4, [[1,2],[2,3],[3,4],[4,2]])
print s.canFinish(6, [[1,6,7,8],[3,2],[2,1]])


