/*
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
*/
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        /* Approach1: Pigen hole or binary search */
		
		int low = 1;
		int high = nums.size()-1;
		int mid, count;
		while(low < high) {
			mid = (low + high)/2;
			count = 0;
			for(int i = 0 ; i < nums.size(); ++i) {
				if(nums[i] <= mid) {
					count += 1;
				}
			}
			printf("mid: %d, count: %d\n", mid, count);
			if (count <= mid) {
				low = mid + 1;
			} else {
				high = mid - 1;
			}
			printf("low: %d, high: %d\n", low, high);
		}
		return low;

		/* Approach 2: Floyd's 2 pointer cycle finding algorithm 
		int slow = 0, fast = 0;
		while(1) {
			fast = nums[nums[fast]];
			slow = nums[slow];
			//cout << "f: " << fast << " slow: " << slow << endl;
			if (fast == slow)
				break;
		}
		int finder = 0;
		while(1) {
			slow = nums[slow];
			finder = nums[finder];
			cout << "f: " << finder << " slow: " << slow << endl;
			if (slow == finder)
				break;
		}
		return slow;
	    */
    }
};
int main() {
	Solution s;
	//int n[] = {1,3,4,2,2};
	int n[] = {9, 9, 8, 7, 6, 5, 4, 3, 2, 1};
	vector<int> nums(n, n + sizeof(n)/sizeof(n[0]));
	cout << s.findDuplicate(nums) << endl;
	return 0;
}
