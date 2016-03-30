'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = coding, word2 = practice, return 3.
Given word1 = "makes", word2 = "coding", return 1.
'''
class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestDistance(self, words, word1, word2):
		w1_last_index = None
		w2_last_index = None
		dis = float('inf')
		for i in range(len(words)):
			if words[i] == word1:	
				if w2_last_index != None:
					d = abs(i - w2_last_index)
					w1_last_index = i
					dis = min(dis, d)
				else:
					w1_last_index = i
			elif words[i] == word2:
				if w1_last_index != None:
					d = abs(i - w1_last_index)
					w2_last_index = i	
					dis = min(dis,d)
				else:
					w2_last_index = i
		return dis

s = Solution()
print s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'practice')
