class Solution:
	#Given array
	'''
	0: 4
	1: 9
	2: 4
	3: 9
	4: 5
	5: 4
	6: 8
	7: 9
	8: 0
	9: 0
	
	goal: count # of cities positioned away from it at each of the distances 0... len(a)-1
 	'''
	#:type a: int[], int
	#:rtype : int[]
	def return_num_nodes_by_inc_hopes(self, a, capital):
		#Create graph: {'A':set(['B', 'C'])}
		# graph: {0: [4, 8, 9], 1: [9], 2: [4], 3: [9], 4: [0, 2, 5], 5: [4] 
		# 			6: [8], 7: [9], 8:[0,6], 9:[0, 1, 3, 7]}
		graph = {}
		for i in range(len(a)):
			if i not in graph:
				graph[i] = set()
			graph[i].add(a[i])
			if a[i] not in graph:
				graph[a[i]] = set()
			graph[a[i]].add(i)

		print "Graph: ", graph
		level = {}
		level[0] = [capital]
		visited = set()
		visited.add(capital)
		self.print_level(capital, graph, 1, level, visited)
	
		print "level: ", level
		res = [0 for i in range(len(a))]
		for l in level:
			res[l] = len(level[l])

		return res

	
	def print_level(self, u, graph, l, level, visited):
		if l not in level:
			level[l] = list()

		for v in graph[u]: 
			if v not in visited:
				if u == 1:
					print v
				level[l].append(v)
				visited.add(v)
				self.print_level(v, graph, l+1, level, visited)

s = Solution()
print s.return_num_nodes_by_inc_hopes([4, 9, 4, 9, 5, 4, 8, 9, 0, 0], 1)
