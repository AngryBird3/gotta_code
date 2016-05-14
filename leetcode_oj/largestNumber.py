'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Hide Tags Sort
Difficulty: Medium
'''
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        if len(num) == 0:
            return "0" 
        # Sort array with out comparision order, in which
        # we'll get num which is higher in given 2 order
        def comp(a, b): 
            s1 = str(a) + str(b)
            s2 = str(b) + str(a)
            if s1 < s2: 
                return -1
            elif s1 > s2: 
                return 1
            else:
                return 0            
        d = sorted(num, cmp=comp)
        result = "".join(str(d[i]) for i in range(len(d)-1, -1, -1))
        return str(int(result))

