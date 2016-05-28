'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.

click to show hint.

Hide Company Tags Microsoft Google Airbnb
Hide Tags Backtracking Trie
Hide Similar Problems (M) Word Search
'''
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        #Create Trie: using new way - dic
        #{'e': {'a': {'t': {'_end': 'end_'}}}, 't': {'r': {'i': {'e': {'_end': 'end_'}}, 'e': {'e': {'_end': 'end_'}}}}}
        if not board or not words:
            return list()
        trie = {}
        for word in words:
            temp = trie
            for w in word:
                if w not in temp:
                    temp[w] = dict()
                temp = temp[w]
            temp['_end'] = 'end_'

        #print "TRIE: "
        #print trie
        #print "--------"
        self.res = list()
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.helper(board, i, j, trie, "") 
        return self.res
        
    def helper(self, board, i, j, trie, word):
        if '_end' in trie and word not in self.res:
            self.res.append(word)
        if board[i][j] not in trie:
            #if i == 0 and j == 1:
                #print "I must not be here: trie: ", trie
            return
                
        trie = trie[board[i][j]]
        temp = board[i][j]
        board[i][j] = " " 
        if '_end' in trie and word+temp not in self.res:
            self.res.append(word+temp)
        if i > 0:
            self.helper(board, i - 1, j, trie, word+temp)
        if i < len(board)-1:
            self.helper(board, i + 1, j, trie, word+temp)
        if j > 0:
            self.helper(board, i, j - 1, trie, word+temp)
        if j < len(board[i]) - 1:
            self.helper(board, i, j + 1, trie, word+temp)
        board[i][j] = temp
