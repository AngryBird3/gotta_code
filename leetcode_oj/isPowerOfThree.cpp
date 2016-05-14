/*
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

Hide Company Tags Google
Hide Tags Math
Hide Similar Problems (E) Power of Two (E) Power of Four
Difficulty: Easy
*/
class Solution {
public:
    bool isPowerOfThree(int n) {
        while (n and n%3 == 0) {
            n/=3;
        }
        return n==1;
    }
};
