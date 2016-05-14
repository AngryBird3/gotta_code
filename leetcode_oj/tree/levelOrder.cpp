/*
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

Hide Company Tags LinkedIn Facebook Amazon Microsoft Apple Bloomberg
Hide Tags Tree Breadth-first Search
Hide Similar Problems (M) Binary Tree Zigzag Level Order Traversal (E) Binary Tree Level Order Traversal II (E) Minimum Depth of Binary Tree (M) Binary Tree Vertical Order Traversal
Difficulty: Easy
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (!root) {
            return vector<vector<int>>();
        }
        queue<TreeNode*> q;
        q.push(root);
        vector<vector<int>> res;
        int i;
        while(!q.empty()) {
            int s = (int)q.size();
            vector<int> l(s);
            //printf("q.size: %d\n", s);
            for (i = 0; i < s; i++) {
                TreeNode *n = q.front();
                //l.push_back(n->val);
                l[i] = n->val;
                //printf("l val: %d\n", n->val);
                q.pop();
                if (n->left) {
                    q.push(n->left);
                }
                if (n->right) {
                    q.push(n->right);
                }
                //printf(" i < s: %d < %d\n", i, (int)s);
            }
            res.push_back(l);
        }
        return res;
    }
};
