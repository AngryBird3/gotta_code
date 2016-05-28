'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:

Try to utilize the property of a BST.
What if you could modify the BST node's structure?
The optimal runtime complexity is O(height of BST).
Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Hide Company Tags Bloomberg Uber Google
Hide Tags Binary Search Tree
Hide Similar Problems (M) Binary Tree Inorder Traversal
Difficulty: Medium
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k): 
        if not root:
            return 0
        if root.left:
            my_id = self.num_of_child(root.left)
            my_id += 1
        else:
            my_id = 1 
        #print my_id
        if my_id  == k:
            return root.val
        return self.kthSmallest_helper(root, k)

    def kthSmallest_helper(self, root, k): 
        # See if its left or right child:
        my_id = self.num_of_child(root.left)
        my_id += 1
        if my_id == k:
            return root.val
        elif my_id > k:
            #search in left
            return self.kthSmallest_helper(root.left, k)
        else:
            return self.kthSmallest_helper(root.right, k - my_id)

    def num_of_child(self, root):
        if not root:
            return 0
        else:
            return 1 + self.num_of_child(root.left) + self.num_of_child(root.right)
