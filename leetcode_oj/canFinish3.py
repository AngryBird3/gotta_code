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
		rec_stack = {}
		#q = deque()
		courses = {}
		p = list()
		for i in range(len(prerequisites)):
			p.append(prerequisites[i][0])
			if prerequisites[i][0] not in courses:
				courses[prerequisites[i][0]] = list()
				visited[prerequisites[i][0]] = False
				rec_stack[prerequisites[i][0]] = False
			for j in range(1, len(prerequisites[i])):
				if prerequisites[i][j] not in courses:
					courses[prerequisites[i][j]] = list()
					visited[prerequisites[i][j]] = False
					rec_stack[prerequisites[i][j]] = False
				courses[prerequisites[i][0]].append(prerequisites[i][j])
		
		#print courses
		assert(len(courses) == numCourses)
		#print p
		#print visited
		for c in p:
			#print "Looking for node: ", c
			if not visited[c]:
				#print "looking for node: ", c
				if self.isCyclic(c, courses, visited, rec_stack):
					return False

		return True

	def isCyclic(self, v, courses, visited, rec_stack):
		if not visited[v]:
			# Mark current node visited
			visited[v] = True
			rec_stack[v] = True
			#print "***"
			#print " node: ", v
			#print "visited: ", visited
			#print " rec_stack: ", rec_stack

			#Recur for all the vertices adjacent to this vertex
			for adj in courses[v]:
				#If an adjacent is not visited, then recur for that adjacent	
				if not visited[adj]:
					if self.isCyclic(adj, courses, visited, rec_stack):
						#print "Returning true for v: ",v, " adj: ", adj
						return True
				elif rec_stack[adj]:
					#print "Found recursion Returning true for v: ",v, " adj: ", adj
					return True
				#else:
				#	return False
		# remove the vertex from recursion stack
		rec_stack[v] = False
		#print "Returning False for node: ", v
		return False
s = Solution()
print s.canFinish(2, [[1,0]])  #TRUE
print s.canFinish(2, [[1,0],[0,1]]) #FALSE
print s.canFinish(3, [[1,2],[2,3]]) #TRUE
print s.canFinish(4, [[1,2,6],[2,3],[3,6]]) #TRUE
print s.canFinish(4, [[1,2],[2,3],[3,4],[4,2]]) #FALSE
print s.canFinish(6, [[1,6,7,8],[3,2],[2,1]]) #TRUE


