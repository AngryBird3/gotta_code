'''
Created on Dec 26, 2012

@author: dharadarji

Given: n x m matrix:
        
Goal: You can move only 1 step either right or 1 step down. 
      Count maximum num of "connected 1" in given matrix.

e.g.
Given: 
        0 0 1 1
        1 1 1 0
        1 0 1 0
        0 1 0 1
Goal:
[Start from top left] maximum no. of 1 is 4
[1,0][1,1][1,2][2,2]
'''

def ConnectedMat(mat, n, m):
    #Allocate
    d=[None]*(n)
    for i in range (n):
        d[i] = [0]*m
    #Initialization
    for i in range(n):
        d[i][0] = mat[i][0]
    for i in range(m):
        d[0][i] = mat[0][i]
    #DP
    maxCount = d[0][0]
    from collections import deque
    path = deque()
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][j] != 0:
                d[i][j] = max(d[i-1][j], d[i][j-1]) + 1
                if maxCount < d[i][j]:
                    maxCount = d[i][j]
                    #For first time, store prev from where we are trying to make move
                    if maxCount == 2:
                        #check left
                        if d[i-1][j] == 1:
                            path.append("["+str(i-1)+","+str(j)+"]")
                            path.append("["+str(i)+","+str(j)+"]")
                        #must be above one
                        else:
                            path.append("["+str(i)+","+str(j-1)+"]")
                            path.append("["+str(i)+","+str(j)+"]")
                    path.append("["+str(i)+","+str(j)+"]")
    print maxCount
    '''
    for i in range(n):
        print d[i][""]
    '''
    print path
mat = [[0,0,1,1],[1,1,1,0],[1,0,1,0],[0,1,0,1]]
ConnectedMat(mat, 4, 4)
                