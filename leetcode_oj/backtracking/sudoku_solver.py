class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.solve(board, 0, 0)

    def solve(self, board, r, c): 
        #If we're running outside of board
        if r > 8:
            return True
        if board[r][c] != '.':
            if c < 8:
                return self.solve(board, r, c + 1)
            else:
                return self.solve(board, r+1, 0)
        #print "i: ", r, " c: ", c
        for num in range(1,10):
            if self.isSafe(r, c, str(num), board):
                board[r][c] = str(num)
                if c < 8:
                    if self.solve(board, r, c+1):
                        #print board[r]
                        return True
                elif self.solve(board, r+1, 0):
                    #print board[r]
                    return True
                board[r][c] = '.'#we're here means this num didnt work out,
        return False
        

    def isSafe(self, row, col, ch, board):
        boxrow = row - row%3
        boxcol = col - col%3
        if self.checkrow(row,ch, board) and self.checkcol(col,ch, board) and self.checksquare(boxrow, boxcol, ch, board):
            return True
        return False

    def checkrow(self, row, ch, board):
        for col in range(9):
            if board[row][col] == ch:
                return False
        return True

    def checkcol(self, col, ch, board):
        for row in range(9):
            if board[row][col] == ch:
                return False
        return True

    def checksquare(self, row, col, ch, board):
        for r in range(row, row+3):
            for c in range(col, col+3):
                if board[r][c] == ch:
                    return False
        return True
