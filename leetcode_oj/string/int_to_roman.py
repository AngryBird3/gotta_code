def intToRoman(num):
		values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
		numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
		res = ""
		for i, v in enumerate(values):
				#print num//v, numerals[i]
				res += (num//v) * numerals[i]
				num %= v
				#print res
				#print num
		return res

#print intToRoman(2012)#MMXII
print intToRoman(36)#XXXVI
