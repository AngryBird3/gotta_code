/*
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
*/

#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;
class Solution {
public:
    int maxSubArrayLen(vector<int>& nums, int k) {
		unordered_map<int, int> m;
		int sum = 0;
		int max_len = 0;
		for (int i = 0; i < nums.size(); i++) {
			sum += nums[i];
			if (sum == k) {
				max_len = max(i+1, max_len);
			} else if (m.find(sum - k) != m.end()) {
				max_len = max(i + 1 - m[sum-k], max_len);
			}
			if (m.find(sum) == m.end()) {
				m[sum] = i+1;
			}
		}	
		return max_len;
    }
};

int main() {
	Solution s;
	int a[] = {1, -1, 5, -2, 3};
	vector<int> v(a, a + sizeof(a));
	int l = s.maxSubArrayLen(v, 2);
	printf("%d\n", l);
}
