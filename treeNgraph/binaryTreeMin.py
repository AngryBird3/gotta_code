'''
Created on Dec 21, 2012

@author: dharadarji

Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height

Algorithm:
----------
- Insert into the tree the middle element of the array
- Insert (into the left subtree) the left subarray elements 
- Insert (into the right subtree) the right subarray elements 
- Recurse
'''

class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        
def addToTree(arr, start, end):
    if end < start:
        return None
    mid = (start + end)/2
    n = TreeNode(arr[mid], None, None)
    n.left = addToTree(arr, start, mid - 1)
    n.right = addToTree(arr, mid + 1, end) 
    print "node: ", n, "data: ", n.data, "left: ", n.left, "right: ", n.right
    return n
    
def binaryTreeMin(arr):
    return addToTree(arr, 0, len(arr) - 1)

arr = [1,3,5,7,9,11,14,15]
binaryTreeMin(arr)