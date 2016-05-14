'''
Implement pow(x, n).
'''
class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1/self.myPow(x, abs(n))
        if n % 2:
            return x*self.myPow(x, n-1)
        else:
            return self.myPow(x*x, n/2)


