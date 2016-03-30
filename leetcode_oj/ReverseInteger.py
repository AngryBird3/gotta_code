import numpy as np
class Solution(object):
	# @return an integer
	def reverse(self, x):
		ii32 = np.iinfo(np.int32)
		if x <= ii32.min or x >= ii32.max:
			return 0;
		if x >= 1073741824 or x <= -1073741824:
                    return 0;
		neg = 1 if x < 0 else 0
		x = abs(x)
		rev_num = 0
		while(x):
			last_dig = x % 10
			rev_num = rev_num * 10 + last_dig
			x = x / 10
		if neg:
			rev_num = 0 - rev_num
		return rev_num

s = Solution()
num1 = 1234
print "Reverse of " , num1 , ": " , s.reverse(num1)
num2 = -5
print "Revertse of " , num2 , ": " , s.reverse(num2)
num3 = 550
print "Revertse of " , num3 , ": " , s.reverse(num3)
num4 = -90
print "Revertse of " , num4 , ": " , s.reverse(num4)
num5 = 1534236469
print "Revertse of " , num5 , ": " , s.reverse(num5)
num5 = 1463847412 
print "Revertse of " , num5 , ": " , s.reverse(num5)
