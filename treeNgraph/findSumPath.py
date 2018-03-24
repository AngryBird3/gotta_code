'''
Created on Dec 22, 2012

@author: dharadarji

Given: Binary tree with each node having value
Goal: Find path (not necessary starting from root) which sums to given value
'''
from compiler.ast import For

class tree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        
'''        
 Constructed binary tree T1 is
             1
           /   \
         2      3
       /  \    /
     4     5  6
    /
   7
'''
node7 = tree(7, None, None)
node4 = tree(4, node7, None)
node5 = tree(5, None, None)
node2 = tree(2, node4, node5)
node6 = tree(6, None, None)
node3 = tree(3, node6, None)
node1 = tree(1, node2, node3)

'''
def findSumPath(currentNode, desiredSum, resultList, level):
    if currentNode == None:
        return
    tmp = desiredSum
    resultList.append(currentNode.data)
    for i in range(level, -1, -1):
        if currentNode.data == 5:
            print "debug: ", resultList
        tmp-=resultList[i]
        if tmp == 0:
            print "Found!"
            printPath(resultList, i, level)
    c1 = resultList
    findSumPath(currentNode.left, desiredSum, c1, level + 1)
    findSumPath(currentNode.right, desiredSum, c1, level + 1)
    
def printPath(resultList, i, level):
    for j in range(i, level+1):
        print resultList[j]
    
def findSum(root, desiredSum):
    result=[]
    findSumPath(root, desiredSum, result, 0)
'''
def findSumPath(currentNode, currentSum, desiredSum, result):
    if currentNode == None:
        return
    currentSum += currentNode.data
    result.append(currentNode.data)
    #print "************ DEBUG: ", result, currentSum 
    if currentSum == desiredSum:
        print "Found!", currentNode.data, currentSum-currentNode.data, result
    result1 = list(result)
    result2 = list(result)
    findSumPath(currentNode.left, currentSum, desiredSum, result1)
    findSumPath(currentNode.right, currentSum, desiredSum, result2)
    resultNew = []
    findSumPath(currentNode.left, 0, desiredSum, resultNew)
    findSumPath(currentNode.right, 0, desiredSum, resultNew)
    
def findSum(root, desiredSum):
    result=[]
    findSumPath(root, 0, desiredSum, result)
    
findSum(node1, 7)