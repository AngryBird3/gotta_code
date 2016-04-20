/*
://leetcode.com/problems/valid-sudoku/
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
*/
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
		/*
		 Algorithm:
			1) Need to make sure if numb is uniq ROW, COLUMN, BOX
			2) Will keep 3 data structure for all of them
			3) row[i][num] = T, for board[i][j] = num
				col[j][num] = T
				box[(i/3) * 3 + (j/3)]

				0   0   0   1   1   1   2   2   2  
				0   0   0   1   1   1   2   2   2  
				0   0   0   1   1   1   2   2   2  
				3   3   3   4   4   4   5   5   5  
				3   3   3   4   4   4   5   5   5  
				3   3   3   4   4   4   5   5   5  
				6   6   6   7   7   7   8   8   8  
				6   6   6   7   7   7   8   8   8  
				6   6   6   7   7   7   8   8   8  
		 */        

		vector<vector<bool>> row(9, vector<bool>(9, false));
		vector<vector<bool>> col(9, vector<bool>(9, false));
		vector<vector<bool>> box(9, vector<bool>(9, false));

		//Or:
		//boolean[][] row = new boolean[9][9];
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				if (board[i][j] == '.') continue;
				int num = board[i][j] - '1'; //It should be between 1 to 9
				int box_num = (i/3) * 3 + (j/3);
				if (row[i][num] || col[j][num] || box[box_num][num]) {
					return false;
				}
				row[i][num] = true;
				col[j][num] = true;
				box[box_num][num] = true;
			}
		}
    }
};

int main() {
	vector<vector<char>> board;
	Solution sol;
	cout << sol.isValidSudoku(board) << "\n";
	return 0;
}
