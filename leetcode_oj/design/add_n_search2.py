class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        root =self.trie
        for w in word:
            if w not in root:
                root[w] = {}
            root = root[w]
        root['_end_'] = True

    def search(self, word, root=None):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not root:
            root = self.trie
        print "search: ", word, " root: ", root
        if not word:
            return '_end_' in root
        for i in range(len(word)):
            if word[i] == ".":
                #print " word: ", word[i+1: ]
                for child in root:
                    exists = self.search(word[i+1:], root[child])
                    if exists:
						return True
                return False
            else:
                if word[i] not in root:
                    return False
                else:
                    #print "i: ", i, " w: ", word[i]
                    root = root[word[i]]
		#print "root: ", root
		return '_end_' in root

# Your WordDictionary object will be instantiated and called as such:
wd = WordDictionary()
wd.addWord("a");wd.addWord("a");
print wd.search(".");
print wd.search("a");
print wd.search("aa");
print wd.search("a");
print wd.search(".a");
print wd.search("a.")
