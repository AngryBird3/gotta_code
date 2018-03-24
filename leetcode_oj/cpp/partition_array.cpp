#include <iostream>
#include <vector>
#include <numeric>

using namespace std;
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int s = std::accumulate(nums.begin(), nums.end(), 0);
        if (s % 2) return false;
        s /= 2;
        int cols = nums.size(); // Extra collumn; considering no element
        vector<vector<int> > opt(s+1, vector<int>(cols));
        opt[0][0] = true;

        for (int j = 1; j < cols + 1; j++) {
            opt[0][j] = true; // Don't know yet,
        }
        for (int i = 1; i < s+1; i++) {
            for (int j = 1; j < cols+1; j++) {
                opt[i][j] = opt[i][j-1]; // not considering current num
                if (i >= nums[j]) {
                    opt[i][j] |= opt[i - nums[j]][j - 1]; // considering current element, if we've solution which sums to (i-nums[j])
                }
            }
        }
        return opt[s][cols];
    }
};

int main() {
  Solution sol;
  vector<int> nums = {1,5,11,5};
  bool res = sol.canPartition(nums);
  cout << res << endl;
}
