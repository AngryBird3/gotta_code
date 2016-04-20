#include <iostream>
#include <vector>
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
    vector<int> rightSideView(TreeNode *root) {
        vector<int> result;
        rightView(root, result, 0);
        return result;
    }

    void rightView(TreeNode *curr, vector<int>& result, int currDepth){
        if(!curr){
            return;
        }
		/*
		cout << "Before appending" << "\n";
		cout << "node: " << curr->val << " currDepth: " << currDepth << "\n";
		copy(result.begin(), result.end(), ostream_iterator<int>(cout, " "));
		cout << "\n";
		cout << "\n";
		*/
        if(currDepth == result.size()){
            result.push_back(curr->val);
        }

        rightView(curr->right, result, currDepth + 1);
		/*
		cout << "After appending" << "\n";
		cout << "node: " << curr->val << " currDepth: " << currDepth << "\n";
		cout << "\n";
		cout << "\n";
		copy(result.begin(), result.end(), ostream_iterator<int>(cout, " "));
		*/
        rightView(curr->left, result, currDepth + 1);

    }
};
int main() {
	Solution sol;
	TreeNode root(1);
	TreeNode t2(2), t3(3), t4(4), t5(5);

	root.left = &t2; root.right = &t3;
	t2.left = &t4; t2.right = &t5;

	vector<int> result = sol.rightSideView(&root);
	copy(result.begin(), result.end(), ostream_iterator<int>(cout, " "));
	cout << "\n";
	return 0;
}
