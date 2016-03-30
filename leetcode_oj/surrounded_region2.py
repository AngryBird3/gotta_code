'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''
class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
	def solve(self, board):
		visited = [[False] * len(board[i]) for i in range(len(board))]
		
		for j in range(len(board[0])):
			if board[0][j] == "O":
				l = list(board[0])
				l[j] = 'B'
				board[0] = ''.join(l)
				#board[0][j] = "B"
		for j in range(len(board[0])):
			if board[len(board)-1][j] == "O":
				#board[len(board)-1][j] = "B"
				l = list(board[len(board)-1])
				l[j] = 'B'
				board[len(board)-1] = ''.join(l)
		for i in range(len(board)):
			if board[i][0] == "O":
				#board[i][0] = "B"
				l = list(board[i])
				l[0] = 'B'
				board[i] = ''.join(l)
		for i in range(len(board)):
			if board[i][len(board[i])-1] == "O":
				#board[i][len(board[i])-1] = "B"
				l = list(board[i])
				l[len(board[i])-1] = 'B'
				board[i] = ''.join(l)

		'''
		for i in range(len(board)):
			print ""
			for j in range(len(board[i])):
				print board[i][j], " ",

		print ""
		'''

		for i in range(len(board)):
			for j in range(len(board[i])):
				if board[i][j] == "O":
					self.convert_os(board, i, j, visited)
				if board[i][j] == "X":
					visited[i][j] = True		

		for i in range(len(board)):
			for j in range(len(board[i])):
				if board[i][j] == "C":
					#board[i][j] = "X"
					l = list(board[i])
					l[j] = 'X'
					board[i] = ''.join(l)
				if board[i][j] == "B":
					l = list(board[i])
					l[j] = "O"
					board[i] = ''.join(l)
					
	def convert_os(self, board, i, j, visited):
		if i <= 0 or i >= len(board)-1 or j <= 0 or j >= len(board[i])-1:
			return
		# If surrounded nodes are visited then mark it X
		if (visited[i+1][j] or board[i+1][j] == "X") and (visited[i-1][j] or board[i-1][j] == "X") and \
				(visited[i][j-1] or board[i][j-1] == "X") and \
				(visited[i][j+1] or board[i][j+1] == "X"):
			#board[i][j] = "X"
			l = list(board[i])
			l[j] = 'X'
			board[i] = ''.join(l)
			visited[i][j] = True
		
		# if visited or are "C" or are 0 (just not last row) then mark them C
		print "[DEBUG: convert to c] i: ", i, " j: ", j
		print "board[i+1][j]: ", board[i+1][j]
		print "board[i-1][j]: ", board[i-1][j]
		print "board[i][j-1]: ", board[i][j-1]
		print "board[i][j+1]: ", board[i][j+1]

		if ((board[i+1][j] == "X" or board[i+1][j] == "O" or board[i+1][j] == "C") and board[i+1][j] != "B") \
				and ((board[i-1][j] == "X" or board[i-1][j] == "C" or board[i-1][j] == "O") and board[i-1][j] != "B") \
				and ((board[i][j-1] == "X" or board[i][j-1] == "C" or board[i][j-1] == "O") and board[i][j-1] != "B") \
				and ((board[i][j+1] == "X" or board[i][j+1] == "C" or board[i][j+1] == "O") and board[i][j+1] != "B"):
			#board[i][j] = "C"
			l = list(board[i])
			l[j] = 'C'
			board[i] = ''.join(l)
			print "[DEBUG: convert to c] i: ", i, " j: ", j

s = Solution()
board = ["OOOO", "OOOO", "OOOO"]
#board = ["XXXX", "XOOX", "XXOX", "XOXX"]
s.solve(board)
print "------"
print "------"
print "------"
for i in range(len(board)):
	print ""
	for j in range(len(board[i])):
		print board[i][j], " ",
