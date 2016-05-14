class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        if divisor == 0 or (dividend == 2147483647 and\
                            divisor == -1): 
            return 2147483647
        sign = 1
        if dividend < 0:
            sign *= -1
            dividend *= -1
        if divisor < 0:
            sign *= -1 
            divisor *= -1

        ans = 0
        while dividend >= divisor:
            a = divisor
            m = 1 
            while ((a << 1) < dividend):
                a <<= 1
                m <<= 1
                print "a: ", a, " m: ", m
            ans += m
            dividend -= a
            print "dividend: ", dividend
        if sign * ans > 2147483647:
            return 2147483647
        if sign * ans < -2147483648:
            return -2147483648
        return sign * ans
s = Solution()
print s.divide(15, 3)
