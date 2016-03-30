'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
'''

class DoublyLinkListNode(object):
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.pre = None
		self.post = None

class DounlyLinkList(object):
	def __init__(self):
		self.head = DoublyLinkListNode(None, None)
		self.tail = DoublyLinkListNode(None, None)
		self.head.pre = None
		self.head.post = self.tail
		self.tail.pre = self.head
		self.tail.post = None

	#Always add node at the beginning
	def addNode(self, node):	
		#Set node's pre and post
		node.pre = self.head
		node.post = self.head.post
	
		#Set head->next pre pointer 
		if self.head.post:
			self.head.post.pre = node
		self.head.post = node

	def removeNode(self, node):
		node.pre.post = node.post
		node.post.pre = node.pre

	#When we're full, pop the last node
	def popTail(self):
		res = self.tail.pre
		print "[DEBUG: popTail] res.key: ", res.key
		self.removeNode(res)	
		return res
	
	#Exist, then move it to head
	def moveToHead(self, node):
		self.removeNode(node)
		self.addNode(node)

class LRUCache(object):
	def __init__(self, capacity):
		"""
		:type capacity: int
		"""
		self.count = 0
		self.capacity = capacity
		self.cache = {}
		self.dq = DounlyLinkList()

	def get(self, key):
		"""
		:rtype: int
		"""
		if not key in self.cache:
			return -1
		node = self.cache[key]
		self.dq.moveToHead(node)
		return node.val
        

	def set(self, key, value):
		"""
		:type key: int
		:type value: int
		:rtype: nothing
		"""
		if key not in self.cache:
			node = DoublyLinkListNode(key, value)	
			self.cache[key] = node
			self.dq.addNode(node)

			self.count += 1
			
			if self.count > self.capacity:
				tail = self.dq.popTail()
				del self.cache[tail.key]
		else:
			#Ok its already there in dq, lets move it to head
			node = self.cache[key]
			node.val = value
			self.dq.moveToHead(node)
			
lru = LRUCache(5)
lru.set(1,"d")
lru.set(3,"d")
lru.set(3,"d")
lru.set(7,"d")
lru.set(8,"d")
lru.set(2,"d")
lru.set(9,"d")
lru.set(1,"d")
lru.set(3,"d")
lru.set(7,"d")
lru.set(7,"d")
lru.set(7,"d")
lru.set(3,"d")
lru.set(2,"d")
lru.set(1,"d")
lru.set(1,"d")
lru.set(1,"d")
lru.set(7,"d")
print lru.get(9)
