#!/usr/bin/env python
class Database():
	""" Handles magic of in-memory database """
	def __init__(self):
		# Stack of transactions with latest on top to accomodate nested         
		# transactions, COMMIT and ROLLBACK
		self.trans = list()	
		# List of num_equal_to for all open trans, top one being latest
		# just like trans data	
		self.list_val_cnt = list()

	def begin(self):
		""" BEGIN new transaction """		
		self.trans.append({})
		self.list_val_cnt.append({})

	def commit(self):
		""" Commit all open transaction (merge forward, the top one is latest)
	    """ 
		if len(self.trans) < 1:
			print "NO TRANSACTION"
			return
		database = {}
		value_counter = {}
		# Going through list of transaction from oldest, as we want database
		# to have latest value for any variabl e
		for t in self.trans:
			for k, v in t.iteritems():
				database[k] = v
		
		for k, v in database.iteritems():
			if v in value_counter:
				value_counter[v] += 1
			else:	
				value_counter[v] = 1	
		self.trans = list()
		self.list_val_cnt = list()
		self.trans.append(database)
		self.list_val_cnt.append(value_counter)

	def rollback(self):
		""" Undo current transaction """ 
		if len(self.trans) <= 1:
			print "NO TRANSACTION"
			return

		self.trans.pop()
		self.list_val_cnt.pop()
		
	def set_var(self, var, val):
		""" Set variable var = value val. Also increment/decrement value
		    counter """ 
		# If we have't begin trans, just begin it anyway
		if not self.trans:
			self.begin()

		cur_value_counter = self.list_val_cnt[-1] 
		#Decrement counter for old value
		old_val = self.get_helper(var)
		if old_val:
			old_val_cnt = self.get_num_equal_to(old_val)
			cur_value_counter[old_val] = old_val_cnt - 1	

		#Increment for new value
		new_val_cnt = self.get_num_equal_to(val)
		#Do it for everything except None
		if val:
			if new_val_cnt:
				cur_value_counter[val] = new_val_cnt + 1
			else:
				cur_value_counter[val] = 1
		
		#Add value to transaction stack (current trans)
		cur_trans = self.trans[-1]
		cur_trans[var] = val

	def get(self, var):
		if self.get_helper(var):
			print self.get_helper(var)
		else:
			print "NULL"

	def get_helper(self, var):
		""" Get value of var if exists """
		# Look into stack of transaction from newest to oldest for var
		for i in range(len(self.trans) - 1, -1, -1):
			t = self.trans[i]
			#print "[DEBUG: GET] ", t
			if var in t:
				return t[var]
		#if var in self.database:
		#	return self.database[var]
		#else:
		return None	

	def unset(self, var):
		""" Unset the variable var, make it NONE """
		self.set_var(var, None)

	def num_equal_to(self, val):
		print self.get_num_equal_to(val)

	def get_num_equal_to(self, val):
		""" Print # of variables that are set to value=val """ 
		if not val:
			return 0 #This is for unset
		# Find it in list of value counter, starting from top
		for i in range(len(self.list_val_cnt) - 1, -1, -1):	
			if val in self.list_val_cnt[i]:
				return self.list_val_cnt[i][val]
		return 0
