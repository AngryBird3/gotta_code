'''
'''
class TicTacToe(object):
    def __init__(self):
        self.board = [['' for j in range(3)] for i in range(3)]
        self.num_of_used_cell = 9
        
    def print_board(self):
        for i in range(3):
            for j in range(3):
                print "-" if not self.board[i][j] else self.board[i][j], 
                if j != 2:
                    print "|",
            print ""

    def update_board(self, r, c, char):
        self.board[r][c] = char
        self.num_of_used_cell -= 1 

    def is_board_full(self):
        return self.num_of_used_cell == 0

    '''
    1) not used cell
    2) not full
    '''
    def move_ai(self):
        if not self.is_board_full():
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '':
                        self.board[i][j] = 'O'
                        self.num_of_used_cell -= 1
                        return
        else:
            raise Exception("Board is full!")

    def is_valid_input(self, r, c):
        if r < 3 and c < 3 and not self.is_board_full() and not self.board[r][c]:
            return True
        return False

    def move(self, r, c):
        if not self.is_valid_input(r, c):
            return 0
        self.update_board(r, c, 'X')

def play_game():
    game = TicTacToe()
    while not game.is_board_full():
        try:
            r, c = map(int, raw_input("Where do you want to place .. enter in r, c: ").split(','))
        except:
            print "Enter valid.."
            continue
        if game.move(r, c) == 0:
            print "Enter valid.."
            continue
        game.move_ai()
        game.print_board()

play_game()
