'''
Created on Feb 21, 2013

@author: dharadarji

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''
class tree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        
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

from collections import deque

def sum_root_to_leaf(root):
    path = {root.data:[root.data]}
    nodes_to_visit = deque([root])
    while len(nodes_to_visit) != 0:
        current_node = nodes_to_visit.popleft()
        if current_node.left != None:
            print "---Left---"
            nodes_to_visit.appendleft(current_node.left)
            print current_node.data, "-", path[current_node.data]
            
            newpath = list(path[current_node.data])
            newpath.append(current_node.left.data)

            path[current_node.left.data] = newpath
            
            print current_node.left.data, "-", path[current_node.left.data]
            
            if current_node.left.left == None and current_node.left.right == None:
                print_sum(path[current_node.left.data])
        if current_node.right != None:
            print "---Right---"
            nodes_to_visit.appendleft(current_node.right)
            print current_node.data, "-", path[current_node.data]
            
            newpath = list(path[current_node.data])
            newpath.append(current_node.right.data)
            path[current_node.right.data] = newpath
            
            print current_node.right.data, "-", path[current_node.right.data]
            
            if current_node.right.left == None and current_node.right.right == None:
                print_sum(path[current_node.right.data])
                
def print_sum(nodes):
    mult = 10 ** (len(nodes) - 1) 
    mysum = 0
    for node in nodes:
        mysum += node * mult
        mult /= 10
        
    print "Sum: ", mysum
    
sum_root_to_leaf(node1)
        
    
