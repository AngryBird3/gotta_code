'''
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
Hide Company Tags Microsoft Bloomberg Facebook
Hide Tags Tree Depth-first Search
Hide Similar Problems (M) Populating Next Right Pointers in Each Node
Difficulty: Hard
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
        q = [root]
        while q:
            size = len(q)
            for i in range(size):
                cur = q.pop(0)
                if i < size-1:
                    cur.next = q[0]
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

    def print_next(self, root):
		if not root:
			return
		print root.val, "->", root.next.val if root.next else "None"
		self.print_next(root.left)
		self.print_next(root.right)
s = Solution()
root = TreeLinkNode(1)
t2 = TreeLinkNode(2); t3 = TreeLinkNode(3)
t4 = TreeLinkNode(4); t5 = TreeLinkNode(5)
t7 = TreeLinkNode(7)
root.left = t2; root.right = t3
t2.left = t4; t2.right = t5; t3.right = t7
s.connect(root)
s.print_next(root)
