'''
Implmenet hash table
'''
import hashlib
class HashTableEntryList:
	'''
	This class represents one entry in hash.
	which has key and value and potential next
	entry pointing next Entry having same key
	(chained hash table)
	'''
	def __init__(self, k, v):
		self.key = k
		self.val = v
		self.next = None

class HashTable:
	# Init: takes care of initializing HashTable
	# where we store HashTableEntryList
	def __init__(self, size=100, resize_factor=2):
		self.size = size
		self.table = [None] * self.size * resize_factor
		self.length = 0
		self.resize_factor = resize_factor 

	# Now to insert key, we need our own
	# Hash function which could generate
	# uniq key value  < self.size
	# Writing myhash so that one can use
	# Inheritance to use their own hash
	def myhash(self, key):
		h = hash(key) 
		if h >= self.size:
			return int(h % self.size)
		if h < 0:
			return int(abs(h) % self.size)	
		return h

	# Insert into hashTable
	# Check size of our table, resize if necessory
	# if key exists in our table, use chaining
	def insert(self, k, v):
		if not k:
			raise ValueError("Key can not be NULL")
		# Resize NOTE: I haven't done rehashing, but I should be
		if self.length >= self.size * self.resize_factor:
			self.table.extend([None for x in xrange(self.size, self.size * 2)])
			self.resize_fector *= 2

		key_index = self.myhash(k)
		if not self.table[key_index]:
			self.table[key_index] = HashTableEntryList(k, v)
			self.length += 1
		else:
			#Chaining
			htel = self.table[key_index]
			while htel.next != None:
				htel = htel.next
			htel.next = HashTableEntryList(k, v)
	
	# return hash[k]	
	def get(self, k):
		key_index = self.myhash(k)
		if not self.table[key_index]:
			raise ValueError("Key not found")

		htel = self.table[key_index]
		while htel:
			if htel.key == k:
				return htel.val
			htel = htel.next		

h = HashTable()
keys = ["Dhara", "Balaji", 28.7, 95, "Boston", 45]
for k in keys:
	h.insert(k, "hey " + str(k))
print "******** Lets print hash ********"
for k in keys:
	print h.get(k)
print h.get("nothere")

