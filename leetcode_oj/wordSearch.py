'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''
class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        if not word:
            return True
        if not board:
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.helper(board, i, j, word):
                    return True
        return False
        
    def helper(self, board, i, j, word):
        if word[0] == board[i][j]:
            if len(word) <= 1:
                return True
            #Mark it as used
            board[i][j] = " " 
            #search next letter in all 4 direction/neighbor
            if i < len(board) - 1 and self.helper(board, i+1, j, word[1:]):
                return True
            if i > 0 and self.helper(board, i-1, j, word[1:]):
                return True
            if j < len(board[i]) - 1 and self.helper(board, i, j+1, word[1:]):
                return True
            if j > 0 and self.helper(board, i, j-1, word[1:]):
                return True
            board[i][j] = word[0] #update the cell to its original value
            return False
        else:
            return False   
