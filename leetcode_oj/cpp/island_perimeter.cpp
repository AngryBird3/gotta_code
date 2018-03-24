#include <iostream>
#include <unordered_map>
#include <vector>
#include <deque>
#include <utility>

using namespace std;

class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int neighbor = 0;
        int count = 0;
        int rows = grid.size() - 1;
        int cols = grid[0].size() - 1;
        for (int i = 0; i < rows + 1; i++) {
            for (int j = 0; j < cols + 1; j++) {
                if (grid[i][j] == 0) continue;
                count += 1;
                if (i < rows && grid[i+1][j]) neighbor++;
                if (j < cols && grid[i][j+1]) neighbor++;
            }
        }
        return (4 * count - 2 * neighbor);
    }
};

int main() {
  Solution sol;
  vector<vector<int>> grid{{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}};
  int p = sol.islandPerimeter(grid);
  cout << p << endl;
  return 0;
}
