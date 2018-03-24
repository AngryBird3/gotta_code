'''
Created on Dec 26, 2012

@author: dharadarji

Given: Binary tree
Goal: Print a binary tree in vertical order using singly linked list

e.g.

 Constructed graph is
             1
           /   \
         2      3 
       /  \    / 
     4     5  6   
    /        /
   7        8 
           /
          9   
We need to check the Horizontal Distances from root for all nodes. 
If two nodes have the same Horizontal Distance (HD), then they are 
on same vertical line. The idea of HD is simple. HD for root is 0, 
a right edge (edge connecting to right subtree) is considered as +1 
horizontal distance and a left edge is considered as -1 horizontal 
distance. For example, in the above tree, HD for Node 4 is at -2, 
HD for Node 2 is -1, HD for 5 and 6 is 0 and HD for node 7 is +2.

*******************************************
******* I really doubt, check 4 and 9****** 
*******************************************   
vertical 
             1(0)
           /   \
          /     \
         /       \ 
        2         3
(0 -1 = -1)       (1)
       /  \       /
     4     5     6(1-1)
(-1-1)    (-1+1)     
    /
   7
(-3)
 0:  1, 5, 6
-1:  2
 1:  3
-2:  4

'''
class tree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        
    def getData(self):
        return self.data
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
'''        
 Constructed binary tree is
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

def printVerticalBinary(root):
    dic={}
    recVerticalBin(root, 0, dic)
    print dic

def recVerticalBin(root, horiDist, dic):
    if root == None:
        return
    'Left'
    recVerticalBin(root.getLeft(), horiDist - 1, dic)
    
    'root'
    #update dic
    if dic.has_key(horiDist):
        mylist = dic[horiDist]
        mylist.append(root.getData())
        dic[horiDist] = mylist
    else:
        mylist = []
        mylist.append(root.getData())
        dic[horiDist] = mylist
        
    'right'
    recVerticalBin(root.getRight(), horiDist + 1, dic)

printVerticalBinary(node1)
    