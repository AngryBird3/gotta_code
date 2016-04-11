/*
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
*/
/**
 * Definition for a binary tree node.
 */
#include <stdio.h>
#include <vector>
#include <queue>
#include <iostream>
#include <unordered_map>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
	unordered_map<int, int> index;
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
    	//Saving index of each element in inorder tree 
		for(int i = 0; i < inorder.size(); i++) {
			index[inorder[i]] = i;
		}
		return helper(inorder, 0, inorder.size()-1, postorder, 0, postorder.size()-1);
    }

	TreeNode* helper(vector<int>& in, int is, int ie, vector<int>& post, int ps, int pe) {
		if (is > ie || ps > pe) {
			return NULL;
		}
		TreeNode *root = new TreeNode(post[pe]);
		int m = index.find(post[pe])->second;

		root->left = helper(in, is, m-1, post, ps, ps + m - is - 1);
		root->right = helper(in, m+1, ie, post, ps + m - is, pe - 1);
		/*
		 Why -is? i.e. inorder start
		 consider: In: 1, 3 ,6; post: 6, 3 ,1
		When 3 is root:
			right (if not -is) - 6 is never considered
			 
		 */
		return root;
	}
};

void print_tree(TreeNode* root) {
	if (!root) return;

	queue<TreeNode*> currentLevel, nextLevel;
	currentLevel.push(root);

	while(!currentLevel.empty()) {
		TreeNode* currNode = currentLevel.front();
		currentLevel.pop();
		if (currNode) {
			cout << currNode->val << " ";
			nextLevel.push(currNode->left);
			nextLevel.push(currNode->right);
		}
		if (currentLevel.empty()) {
			cout << endl;
			swap(currentLevel, nextLevel);
		}
	}
}
int main() {
	vector<int> in{1, 3, 6};
	vector<int> post{6, 3, 1};

	Solution sol;
	TreeNode* root = sol.buildTree(in, post);
	print_tree(root);
}

