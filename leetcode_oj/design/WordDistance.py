'''
This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = coding, word2 = practice, return 3.
Given word1 = makes, word2 = coding, return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''
class WordDistance(object):
	def __init__(self, words):
		"""
		initialize your data structure here.
		:type words: List[str]
		"""
		self.h = {}
		for i in range(len(words)):
			try:
				self.h[words[i]].append(i)
			except:
				self.h[words[i]] = [i]
      	 

	def shortest(self, word1, word2):
		"""
		Adds a word into the data structure.
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		'''
		Algorithm:

		w1_indexes = h[w1]
		w2_indexes = h[w2]

		now, both the indexes are already sort,
		to find minimum distance between those two:
		we could use merge sort concept, think like
		if we've sorted array , finding minimum between
		difference between consecutive : o(n)
		Here, we won't merge but will use it to advance
		indexes
		'''
        
		w1_indexes = self.h[word1]
		w2_indexes = self.h[word2]

		i = 0 #w1_index
		j = 0 #w2_index
		dist = float('inf')
		while i < len(w1_indexes) and j < len(w2_indexes):
			if abs(w1_indexes[i] - w2_indexes[j]) < dist:
				dist = abs(w1_indexes[i] - w2_indexes[j])
			if w1_indexes[i] < w2_indexes[j]:
				i += 1
			else:
				j += 1

		return dist
# Your WordDistance object will be instantiated and called as such:
words = ["practice", "makes", "perfect", "coding", "makes"] 
wordDistance = WordDistance(words)
print wordDistance.shortest("coding", "practice")
print wordDistance.shortest("makes", "coding")

