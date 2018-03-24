#include <iostream>
#include <stdio.h>
#include <vector>

#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;
class Solution {
public:
    vector<vector<char> > updateBoard(vector<vector<char> >& board, vector<int>& click) {
        if (board[click[0]][click[1]] == 'M') {
            board[click[0]][click[1]] = 'X';
            return board;
        }
        updateBoardHelper(board, click[0], click[1]) ;
        return board;
    }

    void updateBoardHelper(vector<vector<char> >& board, int r, int c) {
      if (board[r][c] != 'E') {
          return;
      }
      int mineCount = numOfMines(board, r, c);
      if (mineCount <= 0) {
          board[r][c] = 'B';

          for (int i = r - 1; i < r + 2; i++) {
              for (int j = c - 1; j < c + 2; j++) {
                  if (i == r && j == c) continue;
                  if (i < 0 || j >= board[0].size() || i >= board.size() || j >= board[0].size()) continue;
                  vector<int> neighbor{i,j};
                  updateBoard(board, neighbor);
              }
           }
      } else {
          board[r][c] = '0' + mineCount;
          //printf("Am I here?: board[r][c]: %c\n", board[r][c]);
      }
  }

    int numOfMines(vector<vector<char> >& board, const int r, const int c) {
        int mineCount = 0;
        for (int i = r - 1; i < r + 2; i++) {
            for (int j = c - 1; j < c + 2; j++) {
                if (i == r && j == c) continue;
                if (i < 0 || j >= board[0].size() || i >= board.size() || j >= board[0].size()) continue;
                if (board[i][j] == 'M') {
                    mineCount++;
                }
            }
        }
        if (mineCount > 0) {
          //printf("r=%d, c=%d\n", r, c);
        }
        return mineCount;
    }
};

int main() {
  Solution sol = Solution();
  //{"EEEEE","EEMEE","EEEEE","EEEEE"}
  std::vector<std::vector<char> > board(4, std::vector<char>(5));
  board[0] = {'E', 'E', 'E', 'E', 'E'};
  board[1] = {'E', 'E', 'M', 'E', 'E'};
  board[2] = {'E', 'E', 'E', 'E', 'E'};
  board[3] = {'E', 'E', 'E', 'E', 'E'};
  std::vector<int> click = {3, 0};
  std::vector<std::vector<char> > result = sol.updateBoard(board, click);

  for (const auto& inner : result) {
    for (const auto& item : inner) {
        cout << item << " ";
    }
    cout << endl;
  }

  return 0;
}
