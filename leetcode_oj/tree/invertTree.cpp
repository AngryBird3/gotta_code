/*
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
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
    TreeNode* invertTree(TreeNode* root, TreeNode* head=NULL) {
        if (!root) {
            return head;
        }
        if (!head) {
            head = root;
        }
  
        //Invert: temp = left, left = right, right = left
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        
        //DO same for child nodes
        invertTree(root->left, head);
        invertTree(root->right, head);
    }
};
