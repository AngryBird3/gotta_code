'''
Created on Dec 21, 2012

@author: dharadarji
Given: Binary search tree
Goal: create a linked list of all nodes at each depth
e.g. if you have a tree with depth D, you'll have D linked lists

Algorithm:
Similar to BFS, but keep track of level
'''
class Graph:
    def __init__(self, g):
        self.g = g
    'V: Graph -> Nodes'
    'Returns nodes of Graph G'
    def V(self):
        return self.g.keys()
    'Adj: Graph, Node v -> Adjacent nodes to v'
    'Returns adjacent nodes of node V'
    def Adj(self,v):
        return self.g[v]
    
'''        
 Constructed graph is
             1
           /   \
         2      3
       /  \    /
     4     5  6
    /
   7
'''
graph = {'1':['2','3'],
         '2':['4','5'],
         '3':['6'],
         '4':['7'],
         '5':[],
         '6':[],
         '7':[]}
from collections import deque

def BFS(G,s):
    V = G.V()
    'Storing path of each node'
    prev={}
    'Storing color of each node, 0 in the beginning, 1 when visited' 
    color = {}
    'Queue'
    H = deque()
    for u in V:
        color[u]=0
        prev[u]=None
    color[s]=1
    result = []
    H.append(s)
    H.append("dummy")
    result.append(s) 
    mylist = []
    while(H):
        u = H.popleft() 
        print u       
        if(u == "dummy"):
            print "**** mylist --- ", mylist
            if len(mylist) != 0:
                result.append(mylist)
                mylist = []
        else:
            adjNode = G.Adj(u)
            for v in adjNode:
                if color[v]==0:
                    color[v]=1
                    prev[v]=u
                    print u, "------", v, "-----", H
                    print "mylist --- ", mylist
                    H.append(v)
                    mylist.append(v)
            H.append("dummy")
        
    print result
    
BFS(Graph(graph),'1')