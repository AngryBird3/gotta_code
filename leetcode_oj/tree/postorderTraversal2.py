# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        res = list()
        stack = list()
        stack.append(root)
        visited = {}
        while root:
            stack.append(root.left)    
            root = root.left
        #res.append(node.val)
        #visited[node] = 1
        while stack:
            node = stack.pop()
            if not node:
                continue
            #print "result: ", res, " node: ", node.val
            #Append left most guy
            if (node not in visited) and (not node.left or node.left in visited) and (not node.right or node.right in visited):
                res.append(node.val)
                visited[node] = 1 
                continue
            if node.right:
                stack.append(node)
                stack.append(node.right)
                node = node.right
                while node:
                    stack.append(node.left)
                    node = node.left
        return res 
