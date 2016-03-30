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
		total = 0
		op_stack = list()
		num_stack = list()

		num = 0
		for i in range(len(s)):
			c = s[i]
			if c == " ":
				continue
			if c in "+-(":
				op_stack.append(c)
				continue
			if c == ")":
				op_stack.pop() #for (
				if op_stack:
					if op_stack[-1] == "+":
						total = num_stack.pop() + num_stack.pop()
					else:
						right = num_stack.pop()
						left = num_stack.pop()
						total = left - right 
					op_stack.pop() #for op
					num_stack.append(total)
				continue
			if c.isdigit():
				c = int(c)
				num = num*10 + c
			if i == len(s)-1 or not s[i+1].isdigit():
				#if num:
				#	num_stack.append(num)
				if op_stack and op_stack[-1] in "+-":
					#pop, and do op: with current right operator and left from stack 
					if op_stack[-1] == "+":
						total = num + num_stack.pop()
					else:
						total = num_stack.pop() - num
					op_stack.pop()
					num_stack.append(total)
				else:
					num_stack.append(num)
				num = 0
		return num_stack.pop()

s = Solution()
print s.calculate("(1)   ")
