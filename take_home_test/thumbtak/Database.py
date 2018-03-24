#!/usr/bin/env python
class Database():
	""" Handles magic of in-memory database """
	def __init__(self):
		# This is main database (committed)
		# {key=variable name: value}
		self.database = {}
		# Stack of transactions with latest on top to accomodate nested 
		# transactions, COMMIT and ROLLBACK
		self.trans = list()	
		# Current/latest transaction
		self.latest_trans = {}
		# Keeping counter for current trans
		self.value_counter = {}
		#keeping counter for ALL open trans
		self.value_counter_list = list()

	def begin(self):
		""" BEGIN new transaction """		
		self.trans.append(self.latest_trans)
		self.value_counter_list.append(self.value_counter)
		self.latest_trans = {}
		self.value_counter = {}
		self.no_trans = False

	def commit(self):
		""" Commit all open transaction (merge forward, the top one is latest)
	    """ 
		if not self.trans:
			# If no open transaction; then nothing to do
			print "NO TRANSACTION"
			return
	
		self.trans.append(self.latest_trans)
		# Going through list of transaction from oldest, as we want database
		# to have latest value for any variable
		for t in self.trans:
			print "DEBUG: ", t
			for k, v in t.iteritems():
				self.database[k] = v
		
		self.value_counter = {}
		self.latest_trans = {}
		self.no_trans = True

	def rollback(self):
		""" Undo current transaction """ 
		if not self.latest_trans:
			# If no open transaction; then nothing to do
			print "NO TRANSACTION"
			return
		if self.trans:
			#Pop earlier trans from transaction list
			self.latest_trans = self.trans.pop()
			#Pop older value counter too
			self.value_counter = self.value_counter_list.pop()
		
	def set_c(self, var, val):
		""" Set variable var = value val. Also increment/decrement value
		    counter """ 
		if var in self.latest_trans:
			# As we're changing variable's value, decrement value counter for
			# older value of that variable
			self.value_counter[self.latest_trans[var]] -= 1
		self.latest_trans[var] = val
		# Update value counter value val
		if val in self.value_counter:
			self.value_counter[val] += 1
		else:
			self.value_counter[val] = 1

	def get(self, var):
		""" Get value of var if exists """
		#Check if we current transaction is going on
		if self.latest_trans:
			print self.latest_trans[var] if var in self.latest_trans\
											else "NULL"
		elif var in self.database:
			print self.database[var]
		else:
			print "NULL"	

	def unset(self, var):
		""" Unset the variable var, make it NONE """
		if not self.latest_trans:
			#No current transaction
			return
		if var in self.latest_trans:
			# Decrement value_counter for var's old value 
			self.value_counter[self.latest_trans[var]] -= 1
			self.latest_trans[var] = None
		elif var in self.database:
			self.value_counter[self.database[var]] -= 1
			self.latest_trans[var] = None

	def num_equal_to(self, val):
		""" Print # of variables that are set to value=val """ 
		if val in self.value_counter:
			print self.value_counter[val]
		else:
			print 0

