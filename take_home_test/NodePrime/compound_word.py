import sys
import trie
from argparse import ArgumentParser
class compound_word(object):
	'''
	''' 
	def __init__(self):
		self.my_trie = trie.Trie()	
		self.words = list() 

	#Read from stdin
	def read_input(self):
		for word in sys.stdin:
			self.my_trie.insert(word.strip())
			self.words.append(word.strip())
	
	#Read from file
	def read_file(self, file_name):
		try:
			f = open(file_name, 'r')
			for word in f:
				self.my_trie.insert(word.strip())	
				self.words.append(word.strip())
		except IOError:
			print "Error: can\'t find file or read data"

	# Find if a given word is compund word
	def is_compound_word(self, word):
		#Find prefix(es) and suffix
		#print "[DEBUG: is_compound_word]: ", word
		for i in range(len(word)+1):
			if self.my_trie.search(word[:i]):
				if i >= len(word) or self.is_compound_word(word[i:]):
					return True
		return False	

	# Find longest compund word among the list	
	def find_longset_compound_word(self):
		longest_compound_word = ""
		for w in self.words:
			print ".... word: ", w
			if self.is_compound_word(w):
				if len(w) > len(longest_compound_word):
					longest_compound_word = w

		return longest_compound_word

parser = ArgumentParser()
parser.add_argument("--file_name", help="Input file name (with fullpath)")
parser.add_argument("--c", help="Input words through command line till ctrl-d", action='store_true')
args = parser.parse_args()
comp_w = compound_word()
if args.file_name:
	comp_w.read_file(args.file_name)
elif args.c:
	comp_w.read_input()
else:
	parser.print_help()	
	exit(1)
compound_word = comp_w.find_longset_compound_word() 
print "Longest compound word is: ", compound_word
