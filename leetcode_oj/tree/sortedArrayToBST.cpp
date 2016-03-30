/*
 * Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
 */

#include <stdio.h>
#include<vector>
#include <queue>
#include <iostream>
using namespace std;

/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
		if (nums.size() == 0) {
			return NULL;
		}
		return bst(nums, 0, nums.size()-1);
    }

	TreeNode* bst(vector<int>& nums, int s, int e) {
		if (s > e) {
			return NULL;
		}
		//int mid = s + (e-s)/2;
		int mid = (s+e)/2;
		//printf("Mid: %d, start: %d, end: %d\n", mid,s,e);
		TreeNode* root = new TreeNode(nums[mid]);
		root->left = bst(nums, s, mid - 1);
		root->right = bst(nums, mid+1, e);

		return root;
	}
};

void printLevelOrder(TreeNode *root) {
  if (!root) return;
  queue<TreeNode*> currentLevel, nextLevel;
  currentLevel.push(root);
  while (!currentLevel.empty()) {
    TreeNode *currNode = currentLevel.front();
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
	Solution sol;
	int arr[] = {1,2,3,4};
	vector<int> n(arr, arr + sizeof(arr)/sizeof(arr[0]));

	TreeNode *root = sol.sortedArrayToBST(n);

	//Print by level
	printLevelOrder(root);
}
