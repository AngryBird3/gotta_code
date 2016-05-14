'''
Implement int sqrt(int x).

Compute and return the square root of x.

Bloomberg Apple Facebook
Hide Tags Binary Search Math
Hide Similar Problems (M) Pow(x, n)
Difficulty: Medium
'''
class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x <= 1:
            return x
        left = 0 
        right = (x/2)

        while(left < right):
            mid = (left + right)/2
            s = mid * mid 
            if s == x:
                return mid 
            elif s < x:
                if x < (mid + 1)**2:
                    return mid
                left = mid + 1 
            else:
                right = mid - 1 
        return left
