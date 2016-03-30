# Given two integers representing the numerator and denominator 
# of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating 
# part in parentheses.
# Given numerator = 1, denominator = 2, return "0.5"
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".

class Solution:
	# @return a string
	def fractionToDecimal(self, numerator, denominator):
		a = numerator/float(denominator)
		print a
		int_p = format(a, '.17f').split('.')[0]
		f_to_s = int_p
		try:
			float_p = str(a).split('.')[1]
			f_to_s += "."
		except:
			return f_to_s
		prev = float_p[0]
		count = 1
		for i in range(1, len(float_p)):
			if prev != float_p[i]:
				if count > 1:
					f_to_s += '(' + prev + ')'
				else:
					f_to_s += prev
				prev = float_p[i]	
				count = 1
			else:
				count += 1
		if count > 1:		
			f_to_s += '(' + prev + ')'
		else:
			f_to_s += prev
		return f_to_s	

s = Solution()
#print s.fractionToDecimal(1,2)
#print s.fractionToDecimal(2,1)
#print s.fractionToDecimal(2,3)
#print s.fractionToDecimal(98.6765336, 8)
print s.fractionToDecimal(1, 6)
