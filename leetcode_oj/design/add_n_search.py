'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
'''
class WordDictionary(object):
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		#Looks like: 
		'''
		 {'t':
			{'r':
				{'i':
					{'e': {'_end':'end_', 'a':{ ...} }
					},
				},
			'e':
				{
					'e': {'_end':'end_'} 
				}
			},
			{'a' ..}
		}
		'''
		self.trie = {}
        
	def addWord(self, word):
		"""
		Adds a word into the data structure.
		:type word: str
		:rtype: void
		"""
		temp = self.trie
		for w in word:
			if w not in temp:	
				temp[w] = {}
			temp = temp[w]
		temp['_end'] = 'end_' 
        

	def search(self, word, trie = None):
		"""
		Returns if the word is in the data structure. A word could
		contain the dot character '.' to represent any one letter.
		:type word: str
		:rtype: bool
		"""
		if not trie:
			temp = self.trie
		else:
			temp = trie
		print "word: ", word, " trie: ", temp
		if not isinstance(temp, dict):
			return False
		if word != '_end':
			for i in range(len(word)):
				print "word[i]: ", word[i]
				print " trie: ", temp
				#print "----"
				if word[i] == ".":
					#Search in ALL the 'node' for remainig letter
					if i+1 < len(word):
						#print "word: ", len(word), " trie: ", temp, " word: ", word
						return self.helper(temp, word[i+1:])
					else:	
						return self.helper(temp)
				else:
					if word[i] not in temp:
						return False
					else:
						temp = temp[word[i]]
			return '_end' in temp
			#return True
		else:
			return '_end' in temp
	
	def helper(self, trie, word = None):
		#print "word: ", word, " trie: ", trie
		if not word:
			word = '_end'
		exist = False
		if not isinstance(trie, dict):
			return False
		for k in trie:
			#print "trie[k]: ", trie[k]
			exist = exist or self.search(word, trie[k])
		return exist
	
# Your WordDictionary object will be instantiated and called as such:
w = WordDictionary()
'''
w.addWord("at")
w.addWord("and")
w.addWord("an")
w.addWord("add")
print w.search("a")
print w.search(".at")
w.addWord("bat")
print w.search(".at")
print w.search("an.")
print w.search("a.d.")
print w.search("b.")
print w.search("a.d")
print w.search(".")
'''
'''
w.addWord("bad")
w.addWord("dad")
w.addWord("map")
#w.search("pad")
#w.search("bad")
print w.search(".ad")

'''
'''
#w.addWord("ran")
#w.addWord("rune")
#w.addWord("runner")
#w.addWord("runs")
w.addWord("add")
w.addWord("adds")
w.addWord("adder")
w.addWord("addee")
print w.search(".......")
'''
'''
w.addWord("ran")
w.addWord("rune")
w.addWord("runner")
w.addWord("runs")
w.addWord("add")
w.addWord("adds")
w.addWord("adder")
w.addWord("addee")
#print w.search("r.n")
#print w.search("ru.n.e")
#print w.search("add")
#print w.search("add.")
#print w.search("adde.")
#print w.search(".an.")
#print w.search("...s")
print w.search("....e.")
#print w.search(".......")
#print w.search("..n.r")
'''
w.addWord('a')
print w.search('.')
