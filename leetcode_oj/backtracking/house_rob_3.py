'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
'''
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
	def rob(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		(with_root, without_root) = self.dfs(root)
		return max(with_root, without_root)

	def dfs(self, root):
		if not root:
			return (0, 0)
		with_r_l, without_r_l = self.dfs(root.left)
		with_r_r, without_r_r = self.dfs(root.right)
		without_cur_node = max(with_r_l, without_r_l) +\
							max(with_r_r, without_r_r)
		return (root.val + without_r_l + without_r_r, without_cur_node)

s = Solution()
'''
root = TreeNode(3)
t2 = TreeNode(2)
t3 = TreeNode(3)
t3_1 = TreeNode(3)
t1 = TreeNode(1)

root.left = t2; root.right = t3
t2.right = t3_1; t3.right = t1	
'''
root = TreeNode(3)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
root.left = t2; t2.left = t3; t3.left = t4
print s.rob(root)
