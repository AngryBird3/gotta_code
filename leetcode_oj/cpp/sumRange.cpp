/*
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

*/
#include <stdio.h>
#include <unordered_map>
#include <vector>
using namespace std;
class NumArray {
	// Stores sum till index i
	// where key: index, val: sum from 0 to index
	unordered_map<int, int> sum;
public:
    NumArray(vector<int> &nums) {
		sum[0] = nums[0];
    	for (int i = 1; i < nums.size(); i++) {
			sum[i] = sum[i-1] + nums[i];
		} 
    }

    int sumRange(int i, int j) {
		if (i) 
    		return (sum[j] - sum[i-1]);
		return
			sum[j];
    }
};

int main()
{
	int na[] = {-2, 0, 3, -5, 2, -1};
	vector<int> nums(na, na + sizeof(na)/sizeof(na[0]));
	NumArray num_arr(nums);
	printf("%d\n", num_arr.sumRange(0, 2));
	printf("%d\n", num_arr.sumRange(1, 3));
	printf("%d\n", num_arr.sumRange(2, 5));
	printf("%d\n", num_arr.sumRange(0, 5));
}
