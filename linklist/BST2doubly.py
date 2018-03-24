'''
Created on Feb 15, 2013

@author: dharadarji
Convert a BST to a sorted circular doubly-linked list in-place. 
Think of the left and right pointers as synonymous to the previous 
and next pointers in a doubly-linked list.

NOT WORKING*
'''

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        
def tree_to_doubly(p, prev, head):
    if p == None:
        return
    tree_to_doubly(p.left, prev, head)
    print "current: ", p.data, "prev: ", prev.data if prev!=None else None, "head: ", head.data if head!=None else None
    #current node's left points to prev node
    p.left = prev
    if prev != None:
        prev.right = p #prev node's right points to current node
    else:
        print "Prev is none: ", p.data
        head = p #current node (smallest element) is head of the
                # the list if prev node is not available
    #as soon as recursion ends, the head's left pointer 
    #points to the last node, and the last node's right pointer
    #points to the head pointer
    
    right = p.right
    head.left = p 
    p.right = head
    #update previous node
    prev = p
    tree_to_doubly(right, prev, head)
    print "head: ", head.data, "p: ", p.data, "p left: ", p.left.data, "p right: ", p.right.data

def BST_to_doubly(root):
    prev = None
    head = None
    tree_to_doubly(root, prev, head)
    return head

def print_doubly(head):
    if head != None:
        print "Node value: ", head.data, "left: ", head.left.data, "right: ", head.right.data
    else:
        print "None"
        
'''        
 Constructed binary tree is
             10
           /   \
         7      14
       /  \    /
     4     9  12
    /
   3
'''
node3 = Node(3, None, None)
node4 = Node(4, node3, None)
node9 = Node(9, None, None)
node7 = Node(7, node4, node9)
node12 = Node(12, None, None)
node14 = Node(14, node12, None)
node10 = Node(10, node7, node14)

head = BST_to_doubly(node10)
print_doubly(head)


    