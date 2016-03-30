'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
'''
# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
	def cloneGraph(self, node):
		"""
		:type node: UndirectedGraphNode
		:rtype: UndirectedGraphNode
		"""
		if not node:
			return None
		cg = UndirectedGraphNode(node.label)
		#key: orginal node, val: cloned_node
		d = {node:cg}
		from collections import deque
		q = deque()
		q.append(node)

		while q:
			u = q.popleft()
			print u.label
			for v in u.neighbors:
				if v not in d:
					v_copy = UndirectedGraphNode(v.label)
					d[v] = v_copy
					d[u].neighbors.append(v_copy)
					q.append(v)
				else:
					d[u].neighbors.append(d[v])	
		return cg

n = UndirectedGraphNode(-1)
s = Solution()
s.cloneGraph(n)

