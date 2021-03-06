'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Hide Company Tags LinkedIn Google Facebook Microsoft
Hide Tags Tree Stack Design
Hide Similar Problems (M) Binary Tree Inorder Traversal (M) Flatten 2D Vector (M) Zigzag Iterator (M) Peeking Iterator (M) Inorder Successor in BST
Difficulty: Medium
'''
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.s = list()
        self.left_into_stack(root)
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.s)

    def next(self):
        """
        :rtype: int
        """
        node = self.s.pop()
        self.left_into_stack(node.right)
        return node.val
        
    def left_into_stack(self, root):
        while root:
            self.s.append(root)
            root = root.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
