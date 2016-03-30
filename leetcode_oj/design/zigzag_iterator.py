'''
Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]
It should return [1,4,8,2,5,9,3,6,7].
'''
class ZigzagIterator(object):

	def __init__(self, v1, v2):
		"""
		Initialize your data structure here.
		:type v1: List[int]
		:type v2: List[int]
		"""
       	#Initializing q with all lists in reverse order 
		from collections import deque
		self.q = deque(x[::-1] for x in [v1, v2] if x)

	def next(self):
		"""
		:rtype: int
		"""
		# Pop leftmost list, from there pop rightmost element
		# thats the next element
		# Now append remaining list back to queue tail
		# Hence list will come in 'circular/zigzag' way
		temp = self.q.popleft() #Save temp list
		res = temp.pop() #Our next element
		if temp:
			self.q.append(temp) #Save for next time
		return res 

	def hasNext(self):
		"""
		:rtype: bool
		"""
		return bool(self.q)


# Your ZigzagIterator object will be instantiated and called as such:
v1 = [1,2]
v2 = [3,4,5,6]
i, v = ZigzagIterator(v1, v2), []
while i.hasNext(): v.append(i.next())
print v
