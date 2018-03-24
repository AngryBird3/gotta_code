#import <iostream>
#import <math.h>
class Solution {
public:
    bool isPerfectSquare(int num) {
        int left = 0;
        long right = ceil(num/2);
        long mid;
        while (left <= right) {
            mid = (left+right)/2;
            long sq = mid * mid;
			std::cout << "sq: " << sq << " left: " << left << " right: " << right << " mid: " << mid << "\n";
            if (sq == num) return true;
            if (sq < num) {
                left++;
            } else {
                right--;
            }
        }
        return false;
    }
};

int main() {
	Solution sol;
	bool ans = sol.isPerfectSquare(2147395600);
	std::cout << ans << "\n";
}
