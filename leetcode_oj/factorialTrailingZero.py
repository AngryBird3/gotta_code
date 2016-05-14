'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Hide Company Tags Bloomberg
Hide Tags Math
Hide Similar Problems (H) Number of Digit One
Difficulty: Easy
'''
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        if n <= 0:
            return 0
        if n == 5:
            return 1
        num_zero = 0
        i = 5
        while (math.ceil(n/i) >= 1):
            num_zero += math.ceil(n/i)
            i *= 5
        return int(num_zero)
        
