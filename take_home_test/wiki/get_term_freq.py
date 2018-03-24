#!/user/bin/env python
'''
Created on Dec 12, 2015

@author: DHARA
'''
import indexing1
import re, os
#@doc: This class is reading data from catalog
class get_term_freq:
	'''
	INTERP: Get freq of term in corpus
	term is string
	'''
	def __init__(self, data_path, catalog_file, index_file):
		self.catalog_file = catalog_file
		self.index_file = index_file
		#Create indexing if it doesn't exists already
		if not os.path.exists(catalog_file):
			index_obj = indexing1.indexing1(data_path, index_file, catalog_file)
			index_obj.create_indexing()

	def get_freq(self, term):	
		cfile = open(self.catalog_file, 'r')
		#line = re.findall(r'\b%s\b.*' %(term),''.join(cfile.readlines()),re.I)
		line = re.split('\W+', \
					''.join(\
						re.findall(r'\b%s\b.*' %(term), ''.join(cfile.readlines()), re.I)))
		#print "[DEBUG: line from index]: ", line
		cfile.close()	
		
		'''
		Its possible we match more than one lines
		e.g. down, or down! 
		we've to merge all the results
		freq = 0
		ofile = open(self.index_file, 'r')
		for l in line:
			ofile.seek(int(l[1]))
			data = ofile.readline().split()[1]
			print "[DEBUG: data] ", data
			ofile += int(data)
		return freq
		'''
		ofile = open(self.index_file, 'r')
		ofile.seek(int(line[1]))
		data = re.findall(r'[A-Za-z0-9\-]+',ofile.readline())
		#print "[DEBUG: get_freq] reading data", data
		return data[1]

