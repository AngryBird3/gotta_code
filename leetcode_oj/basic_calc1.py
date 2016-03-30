'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
'''
class Solution(object):
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		sign = 1
		total = 0
		stack = list()
		num = 0

		for c in s:
			if c == " ":
				continue
			if c.isdigit():
				num = num*10 + int(c)
				continue
			if c == "+":
				#Num is over add it	
				total += sign * num
				num = 0
				sign = 1
			if c == "-":
				total += sign * num
				num = 0
				sign = -1
			if c == "(":
				#push sign and total onto stack for later ues
				stack.append(sign)
				stack.append(total)
				num = 0
				total = 0
				sign = 1
			if c == ")":
				total += sign * num
				prev_total = stack.pop()
				prev_sign = stack.pop()
				total *= prev_sign
				total += prev_total
				num = 0
		total += sign * num
		return total

s = Solution()
print s.calculate("(1+4)-7   ")
