/*
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
*/
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
 		/*
		 do:
			start = 0
			if nums[i] != 0:
				copy ith to start
			else:
				count num_of_zeros
		 while we reach at the end
		 append num_of_zeros
		 */       
		if (nums.empty()) return;
		int start = 0, i =0;
		while (i < nums.size()) {
			if (nums[i]) {
				nums[start] = nums[i];	
				start++;
			}
			i++;
		}
		while(start < nums.size()) {
			nums[start] = 0;
			start++;
		}
    }
};

void print_zeros(vector<int> myvector) {
	for (int i = 0; i < myvector.size(); i++) {
		cout << myvector[i] << ", ";
	}
	cout << endl;
}

int main() {
	// empty;
	Solution s;
	vector<int> myvector;
	s.moveZeroes(myvector);
	cout << "After moveZeros: " << endl;
 	print_zeros(myvector);
	//Non empty
	int myints[] = {0, 1, 0, 3, 12};
  	vector<int> nonempty (myints, myints + sizeof(myints) / sizeof(int) );
	s.moveZeroes(nonempty);
	cout << "After moveZeros: " << endl;
	print_zeros(nonempty);
	return 0;
}
