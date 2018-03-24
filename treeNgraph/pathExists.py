'''
Created on Dec 21, 2012

@author: dharadarji
Goal: Given a directed graph, design an algorithm to find out whether there is a route between two nodes
Sol: Any graph traversal algo, doing BFS
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
    
myGraph={'s':['a','b','c','d','t'],
         'a':['s','b','c','d','t'],
         'b':['a','s','c','d','t'],
         'c':['a','b','s','d','t'],
         'd':['a','b','c','s','t'],
         't':['a','b','c','d','s']} 

from collections import deque

def BFS(G,s,t):
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
    
    H.append(s) 
    while(H and prev[t] == None):
        u = H.popleft()        
        
        adjNode = G.Adj(u)
        for v in adjNode:
            if color[v]==0:
                if v == t:
                    return True
                else:
                    color[v]=1
                    prev[v]=u
                    H.append(v)
                
    'print str(prev)' 
    
#print BFS(Graph(myGraph), 's', 't')
print BFS(Graph(graph), '1', '7')