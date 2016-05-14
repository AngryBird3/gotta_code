/*
Given an integer, write a function to determine if it is a power of two.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Hide Company Tags Google
Hide Tags Math Bit Manipulation
Hide Similar Problems (E) Number of 1 Bits (E) Power of Three (E) Power of Four
Difficulty: Easy
*/
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n>0 && (n & (n-1)) == 0) return true;
        return false;
    }
};
