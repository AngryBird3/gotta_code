/*
You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

Example 1:
Given x = [2, 1, 1, 2],
┌───┐
│   │
└───┼──>
    │

Return true (self crossing)
Example 2:
Given x = [1, 2, 3, 4],
┌──────┐
│      │
│
│
└────────────>

Return false (not self crossing)
Example 3:
Given x = [1, 1, 1, 1],
┌───┐
│   │
└───┼>

Return true (self crossing)
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

Hide Tags Math
Difficulty: Hard
*/
class Solution {
public:
    bool isSelfCrossing(vector<int>& x) {
        int i;
        for (i = 3; i < x.size(); i++) {
            /*
              ------
              |     |
              |     |
              ------|---
                    |
             */
            // 4th line is crossing 4-4th
            // 4th line has to go beyond 2nd line
            // 3rd line has to be <= 1th line
            if (x[i] >= x[i-2] && x[i-1] <= x[i-3]) return true;

            //5th crossing 1st
            /*
              ------
              |     |
              |     |
              |     |
              ------
             */
            if (i >= 4) {
                // 5th + 1st >= 3rd 
                // 2nd line == 4th line
                if (x[i] + x[i-4] >= x[i-2] &&
                        x[i-3] == x[i-1]) return true;
            }   

            //6th crossing 1st
            if (i >= 5) {
                //6th >= 4th - 2nd
                //5th >= 3rd - 1st
                //of course 5th <= 3rd
                if (x[i-2] > x[i-4] &&
                    x[i] >= x[i-2] - x[i-4] &&
                    x[i-1] >= x[i-3] - x[i-5] &&
                    x[i-1] <= x[i-3]) return true;  
            }   
        }   
        return false;
    }
};
