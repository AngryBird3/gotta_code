class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        if board == None or len(board) == 0:
            return 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    self.merge(board, i, j)

    def merge(self, board, i, j): 
        if i <= 0 or j <= 0 or i >= (len(board) - 1) or j >= (len(board[i]) - 1): 
            return
        if board[i][j] != 'O':
            return
        l = list(board[i])
        l[j] = 'X'
        board[i] = ''.join(l)
        #board[i][j] = 'X' 
        self.merge(board, i - 1, j)
        self.merge(board, i + 1, j)
        self.merge(board, i, j - 1)
        self.merge(board, i, j + 1)
s = Solution()
board = ["OOOO", "OOOO", "OOOO"]
s.solve(board)
for i in range(len(board)):
	print ""
	for j in range(len(board[i])):
		print board[i][j], " ",
