#!/user/bin/env python
'''
Created on Dec 12, 2015

@author: DHARA
'''
import os, re
class indexing1:
	'''
	data_dir_path: Directory path where data resides
	index_path: type string: File path to store word/freq
	catalog_path: type string: File path to store where word resides in index.txt
	read_order: type list of char: Alphabets order to optimize indexing
	'''
	ALPHABETS = ['a','b','c','d','e','f','g','h','i','j','k','k','m','n','o','p','q','r',\
					's','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
	def __init__(self, data_dir_path, index_path, catalog_path, read_order=ALPHABETS):
		self.data = data_dir_path
		self.index_file = index_path
		self.catalog_file = catalog_path

	'''
	read_data: Yield list of files in directory
	'''
	def read_data_directory(self):
		for root, dirs, files in os.walk(self.data):
			for names in files:
				yield os.path.join(root, names)

	'''
	Create indexing
	'''
	def create_indexing(self):
		for a in self.ALPHABETS:
			term_freq = {}
			for f in self.read_data_directory():
				with open(f, 'r') as f:
					for line in f:
						for s in line.split():
							# Remove extra char
							try:
								word = re.findall("\w+", s)[0]
							except:
								pass
							# We only care if this word starts with current alphabet a
							if word[0] != a:
								continue
							# If we wanna do stemming now is the time
							if term_freq.has_key(word):
								term_freq[word] += 1
							else:
								term_freq[word] = 1

		
			#Lets save term_frq into index file
			#And save 'index' of word into catalog
			ofile = open(self.index_file, 'a')
			cfile = open(self.catalog_file, 'a') 
			for term in term_freq:
				start = ofile.tell()
				ofile.write("%s		%s\n" %(term, repr(term_freq[term])))
				end = ofile.tell()
				cfile.write("%s		%s		%s\n" % (term,start,end))
			ofile.close()
			cfile.close()
