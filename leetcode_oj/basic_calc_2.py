'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
'''
class Solution(object):
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		stack = list()
		sign = "+"
		num = 0
		#Do "*" and "/" operations first, at the end sum(stack) = Ans
		for i in range(len(s)):
			c = s[i]
			if c.isdigit():
				num = num*10 + int(c)
			if i == len(s) - 1 or (c != " " and not c.isdigit()):
				if sign == "+":
					stack.append(num)
				if sign == "-":
					stack.append(-num)	
				if sign == "*":
					stack.append(stack.pop() * num)
				if sign == "/":
					if stack[-1] < 0 and stack[-1] % num != 0:
						stack.append(stack.pop()//num+1)
					else:
						stack.append(stack.pop() // num)
				sign = c
				num = 0
		return sum(stack)
s = Solution()
print s.calculate("14-3/2")
