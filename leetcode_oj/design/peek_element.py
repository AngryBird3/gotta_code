'''
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

Call next() gets you 1, the first element in the list.

Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.

Hint:

Think of "looking ahead". You want to cache the next element.
Is one variable sufficient? Why or why not?
Test your design with call order of peek() before next() vs next() before peek().Show More Hint 
Follow up: How would you extend your design to be generic and work with all types, not just integer?
'''

# Below is the interface for Iterator, which is already defined for you.

class Iterator(object):
	def __init__(self, nums):
		"""
		Initializes an iterator object to the beginning of a list.
		:type nums: List[int]
		"""
		self.l = nums

	def hasNext(self):
		"""
		Returns true if the iteration has more elements.
		:rtype: bool
		"""
		return bool(self.l)

	def next(self):
		"""
		Returns the next element in the iteration.
		:rtype: int
		"""
		return self.l.pop(0)

class PeekingIterator(object):
	def __init__(self, iterator):
		"""
		Initialize your data structure here.
		:type iterator: Iterator
		"""
		self.itr = iterator
		self.has_peeked = False
		self.peek_elem = None

	def peek(self):
		"""
		Returns the next element in the iteration without advancing the iterator.
		:rtype: int
		"""
		if self.has_peeked:
			return self.peek_elem
		self.peek_elem = self.itr.next() if self.itr.hasNext() else None
		self.has_peeked = True
		return self.peek_elem
        

	def next(self):
		"""
		:rtype: int
		"""
		if self.has_peeked:
			self.has_peeked = False
			return self.peek_elem
		else:
			self.has_peeked = False
			return self.itr.next()

	def hasNext(self):
		"""
		:rtype: bool
		"""
		return self.has_peeked or self.itr.hasNext() 

# Your PeekingIterator object will be instantiated and called as such:
nums = [1,2,3,4]
iter = PeekingIterator(Iterator(nums))
while iter.hasNext():
	val = iter.peek()   # Get the next element but not advance the iterator.
	print "val: ", val
	iter.next()         # Should return the same value as [val].
