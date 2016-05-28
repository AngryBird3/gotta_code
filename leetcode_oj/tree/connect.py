'''
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
Hide Company Tags Microsoft
Hide Tags Tree Depth-first Search
Hide Similar Problems (H) Populating Next Right Pointers in Each Node II (M) Binary Tree Right Side View
Difficulty: Medium
'''
# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        root.next = None
        self.helper(root, None)
        
    def helper(self, node, sib):
        if not node:
            return
        if node.left:
            node.left.next = node.right
            node.right.next = sib.left if sib else None
        self.helper(node.left, node.right)
        self.helper(node.right, None)
	
    def print_next(self, root):
		if not root:
			return
		print root.val, "->", root.next.val if root.next else "None"
		self.print_next(root.left)
		self.print_next(root.right)

s = Solution()
root = TreeLinkNode(-1)
zero = TreeLinkNode(0); one = TreeLinkNode(1)
two = TreeLinkNode(2); three = TreeLinkNode(3)
three = TreeLinkNode(3); four = TreeLinkNode(4)
four = TreeLinkNode(4); five = TreeLinkNode(5)
six = TreeLinkNode(6); seven = TreeLinkNode(7)
eight = TreeLinkNode(8); nine = TreeLinkNode(9)
ten = TreeLinkNode(10); eleven = TreeLinkNode(11)
root.left = zero; root.right = one
zero.left = two; zero.right = three
one.left = four; one.right = five;
two.left = six; two.right = seven;
three.left = eight; three.right = nine
four.left = ten; four.right = eleven
s.connect(root)
s.print_next(root)
