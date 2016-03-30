'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''
class MinStack:
    # @param x, an integer
    # @return an integer
	def push(self, x):
		self.stack.append(x)
		if len(self.minimum_stack) == 0 or x <= self.minimum_stack[-1]:
			self.minimum_stack.append(x)

	# @return nothing
	def pop(self):
		top = self.stack.pop()
		if top == self.minimum_stack[-1]:
			self.minimum_stack.pop()

	# @return an integer
	def top(self):
		return self.stack[-1]
        
	# @return an integer
	def getMin(self):
		return self.minimum_stack[-1]
	
	def __init__(self):
		self.minimum_stack = list()
		self.stack = list()

s = MinStack()
s.push(-2)
s.push(0)
s.push(-1)
print s.getMin()
print s.top()
s.pop()
print s.getMin()

