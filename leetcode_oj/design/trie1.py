'''
Implement a trie with insert, search, and startsWith methods.
Note: You may assume that all inputs are consist of lowercase letters a-z.
'''
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
		self.links = [None] * 26
		self.fullword = False 

class Trie:

	def __init__(self):
		self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
	def insert(self, word):
		node = self.root
		for w in word:
			c = ord(w) % 26	
			if not node.links[c]:
				node.links[c] = TrieNode()
			node = node.links[c]
		node.fullword = True
		
    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
	def search(self, word):
		node = self.root 
		for w in word:
			c = ord(w) % 26
			if not node.links[c]:
				return False
			node = node.links[c]
		return node.fullword

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
	def startsWith(self, prefix):
		node = self.root
		for w in prefix:
			c = ord(w) % 26
			if not node.links[c]:
				return False
			node = node.links[c] 
		return True

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
trie.insert("dhara")
trie.insert("tree")
trie.insert("trie")
trie.insert("trieste")
trie.insert("dolphin")
trie.insert("dharma")
trie.insert("balaji")
print "tree: ", trie.search("tree")
print "balaji: ", trie.search("balaji")
print "trieste: ", trie.search("trieste")
print "some: ", trie.search("some")


print "starting with so: ", trie.startsWith("so")
print "starting with balaji: ", trie.startsWith("balaji")
print "starting with is: ", trie.startsWith("is")
print "starting with trees: ", trie.startsWith("trees")
