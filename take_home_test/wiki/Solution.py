#!/user/bin/env python
'''
Created on Dec 12, 2015

@author: DHARA
'''
import get_term_freq

class Solution():
	INDEX_PATH = "index_file.txt"
	CATALOG_PATH = "catalog_file.txt"

	def __init__(self, data_path, index_path=INDEX_PATH, catalog_path=CATALOG_PATH):
		self.get_term_obj = get_term_freq.get_term_freq(data_path, catalog_path, index_path)

	def freq(self, term):
		print self.get_term_obj.get_freq(term)

import sys
#Can be replaced with argparse
if len(sys.argv) != 2:
	print "Usage: Python Solution.py <term>"
	exit(0)
s = Solution('data')
s.freq(sys.argv[1])
