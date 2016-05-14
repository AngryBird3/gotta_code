#import numpy as np
class Solution(object):
        # @return an integer
        def reverse(self, x): 
                #ii32 = np.iinfo(np.int32)
                #if x <= ii32.min or x >= ii32.max:
                #        return 0;
                rev_num = 0
                neg = -1 if x < 0 else 1
                x = abs(x)
                while x != 0:
                        rev_num = rev_num * 10 + x % 10
                        #print rev_num
                        x = x / 10
                return 0 if rev_num >= 2147483647 or rev_num <= -2147483648 else (neg * rev_num)

s = Solution()

