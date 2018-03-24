'''
Created on Jan 13, 2013

@author: dharadarji

Given two integers n and k, return all possible combinations of k 
numbers out of 1 ... n.
'''
from collections import deque
def dfs(ret, tmp, n, left, k):
    if k == 0:
        ret.append(tmp)
        print tmp
        return
    for i in range(left, n+1):
        #print "i ", i, " left ", left, " k ", k, "ret-", ret, "tmp- ", tmp
        tmp.append(i)
        dfs(ret, tmp, n, i + 1, k - 1)
        tmp.pop()
        #print "After pop,... i ", i, " left ", left, " k ", k, "ret-", ret, "tmp- ", tmp
        

def combine(n, k):
    ret = deque()
    tmp = deque()
    dfs(ret, tmp, n, 1, k)
    
combine(4, 2)