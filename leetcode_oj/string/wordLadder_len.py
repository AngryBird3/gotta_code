'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
'''
class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        if not beginWord or not endWord or not wordDict:
            return 0
        # word : path_count
        table = {beginWord:1}
        alphabets = set("abcdefghijklmnopqrstuvwxyz")
        while table:
            temp_table = table.copy() #To avoid: RuntimeError: dictionary changed size during iteration
            for word, count in temp_table.viewitems():
                del table[word] 
                # if current word can be transformed into end, then we're done
                if self.lastWord(word, endWord):
                    return count + 1 
                else:
                    # if not then convert into dict word
                    for i in range(len(word)):  
                        for c in alphabets:
                            # Replace ith word with alaphabets
                            next_word = word[:i] + c + word[i+1:]
                            if next_word in wordDict:
                                table[next_word] = count + 1 
                                wordDict.remove(next_word) #Can not use one word twice
        return 0

    def lastWord(self, word, end):
        diff = 0 
        for i in range(len(word)):
            if word[i] != end[i]:
                diff += 1
        if diff > 1:
            return False
        else:
            return True 
