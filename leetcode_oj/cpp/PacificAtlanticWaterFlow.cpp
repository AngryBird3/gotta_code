#include <vector>

#include <iostream>
#include <stdio.h>
#include <vector>
#include <deque>

using namespace std;

class Solution {
public:
    vector<pair<int, int>> pacificAtlantic(vector<vector<int>>& matrix) {
        vector<pair<int, int>> common;
        std::deque<std::tuple<int, int> > pacific_cells;
        std::deque<std::tuple<int, int> > atlantic_cells;
        vector<vector<int>> visited_pacific(matrix.size(), vector<int> (matrix[0].size()));
        vector<vector<int>> visited_atlantic(matrix.size(), vector<int> (matrix[0].size()));
        int rows = matrix.size();
        int cols = matrix[0].size();

        for(int i = 0; i < rows; i++)
        {
            visited_atlantic[i][cols-1] = visited_pacific[i][0] = 1;
            atlantic_cells.push_back(make_pair(i,cols-1));
            pacific_cells.push_back(make_pair(i,0));
        }

        for(int i = 0; i < cols; i++)
        {
            visited_atlantic[rows-1][i] = visited_pacific[0][i] = 1;
            atlantic_cells.push_back(make_pair(rows-1,i));
            pacific_cells.push_back(make_pair(0,i));
        }


        do_bfs(matrix, pacific_cells, visited_pacific);
        do_bfs(matrix, atlantic_cells, visited_atlantic);
        cout << " Visited pacific_cells " << endl;

        for (const auto& inner : visited_pacific) {
            for (const auto& item : inner) {
                  cout << item << " ";
            }
            cout << endl;
        }

        //std::set_intersection(pacific_cells.begin(), pacific_cells.end(),
        //                        atlantic_cells.begin(), atlantic_cells.end(),
        //                        std::back_inserter(common));
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (visited_atlantic[i][j] && visited_pacific[i][j] ) {
                    common.push_back(std::make_pair(i, j));
                }
            }
        }

        return common;
    }

    void do_bfs(vector<vector<int>>& matrix, std::deque<std::tuple<int, int> >& q, vector<vector<int>>& visited) {
        while(!q.empty()) {
            std::tuple<int, int> cell = q.front();
            q.pop_front();
            int r = std::get<0>(cell);
            int c = std::get<1>(cell);
            int rows = matrix.size();
            int cols = matrix[0].size();

            //right
            if (c + 1 < cols && visited[r][c + 1] == 0 && matrix[r][c + 1] >= matrix[r][c]) {
                q.push_back(std::make_tuple(r, c + 1));
                visited[r][c + 1] = 1;
                //flood.insert(std::make_tuple(r, c + 1));
            }
            //left
            if (c > 0 && visited[r][c - 1] == 0 && matrix[r][c - 1] >= matrix[r][c]) {
                q.push_back(std::make_tuple(r, c - 1));
                visited[r][c - 1] = 1;
                //flood.insert(std::make_tuple(r, c - 1));
            }
            //down
            if (r + 1 < rows && visited[r + 1][c] == 0 && matrix[r + 1][c] >= matrix[r][c]) {
                q.push_back(std::make_tuple(r + 1, c));
                visited[r + 1][c] = 1;
                //flood.insert(std::make_tuple(r + 1, c));
            }
            //up
            if (r > 0 && visited[r - 1][c] == 0 && matrix[r - 1][c] >= matrix[r][c]) {
                q.push_back(std::make_tuple(r - 1, c));
                visited[r - 1][c] = 1;
                //flood.insert(std::make_tuple(r - 1, c));
            }
        }
    }
};

int main() {
  Solution sol;
  std::vector<std::vector<int> > matrix(5, std::vector<int>(5));
  matrix[0] = {1,2,2,3,5};
  matrix[1] = {3,2,3,4,4};
  matrix[2] = {2,4,5,3,1};
  matrix[3] = {6,7,1,4,5};
  matrix[4] = {5,1,1,2,4};

  vector<pair<int, int>> common = sol.pacificAtlantic(matrix);
  return 0;
}
