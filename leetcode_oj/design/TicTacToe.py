'''

'''
class TicTacToe(object):
	def __init__(self, n):
		"""
		:type n: int
		"""
		self.row = [0] * n
		self.col = [0] * n
		self.diag1 = 0
		self.diag2 = 0
		self.n = n
		self.used = [[0 for j in range(n)] for i in range(n)]
		self.total_num_of_cell = n * n
    
	def move(self, row, col, player):
		"""
		Player {player} makes a move at ({row}, {col}).
		@param `row The row of the board.
		@param col The column of the board.
		@param player The player, can be either 1 or 2.
		@return The current winning condition, can be either:
				0: No one wins.
				1: Player 1 wins.
				2: Player 2 wins.
		:type row: int
		:type col: int
		:type player: int
		:rtype: int
		"""
		add = 1 if player == 1 else -1
		self.row[row] += add
		self.col[col] += add
		if row == col:
			self.diag1 += add
		if row + col == self.n - 1:
			self.diag2 += add
		if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diag1) == self.n or abs(self.diag2) == self.n:
			return player
		return 0

	def is_valid_move(self, row, col):
		"""
		"""
		if  row >= self.n or col >= self.n or self.used[row][col]:
			return 0
		else:
			self.used[row][col] = 1
			self.total_num_of_cell -= 1
			return 1

	def is_game_over(self):
		"""
		"""
		return self.total_num_of_cell == 0

def play_tic_tac_toe():
	n = raw_input("Square size?: ")
	tic_tac_toe = TicTacToe(int(n))
	player = 1 #1st player, 2nd player = -1
	print "Let's play the game then! start with first player and then it will assume to alternate"
	while not tic_tac_toe.is_game_over():
		cell = raw_input("which cell - enter row, col: ")
		try:
			r, c = map(int, cell.split(","))	
		except:
			print "Invalid input, try again"
			continue
		if not tic_tac_toe.is_valid_move(r, c):
			print "Please use unused cell which is valid!!"
			continue
		if tic_tac_toe.move(r, c, player) != 0:
			print "Woot! you just won, my friend!"
			break
		player *= -1

play_tic_tac_toe()		
