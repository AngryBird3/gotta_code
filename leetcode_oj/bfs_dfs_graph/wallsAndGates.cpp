/*
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
*/
#include <tuple>
#include <stdio.h>
#include <iostream>
#include <queue>
#include <limits.h>
#include <vector>

using namespace std;

class Solution {
public:
    void wallsAndGates(vector<vector<int> >& rooms) {
		int i, j;
		queue<tuple<int, int> > q;
		
		for (i = 0; i < rooms.size(); i++) {
			for (j = 0; j < rooms[i].size(); j++) {
				if (rooms[i][j] == 0) {
					q.push(make_tuple(i, j));
				}
			}
		}	
        
		bfs(q, rooms);

		//Replace 0 with INF
		/*
		for ( i = 0; i < rooms.size(); i++) {
			for ( j = 0; j < rooms[i].size(); j++) {
				if (rooms[i][j] == ) {
					rooms[i][j] = INT_MAX;
				}
			}
		}
		*/
    }

	void bfs(queue<tuple<int, int> > &q, vector<vector<int> >& grid) {
		int i, j;
	
		while (!q.empty()) {
			tie(i, j) = q.front();
			q.pop();
			
			printf("Q pop: [%d][%d]\n", i, j);
			//Go around
			if (i < grid.size() - 1 && grid[i+1][j] > 0 ) {
				if (grid[i][j] < INT_MAX - 1 && grid[i+1][j] > grid[i][j] + 1) {
					grid[i+1][j] = grid[i][j] + 1;
					q.push(make_tuple(i+1, j));
					//printf("Update for [%d][%d]\n", i+1, j);
				}
			}
			if (i > 0 && grid[i-1][j] > 0 ) {
				if (grid[i][j] < INT_MAX - 1 && grid[i-1][j] > grid[i][j] + 1) {
					grid[i-1][j] = grid[i][j] + 1;
					q.push(make_tuple(i-1, j));
					//printf("Update for [%d][%d]\n", i-1, j);
				}
			}
			if (j < grid[i].size()-1 && grid[i][j+1] > 0 ) {
				if (grid[i][j] < INT_MAX - 1 && grid[i][j+1] > grid[i][j] + 1) {
					grid[i][j+1] = grid[i][j] + 1;
					q.push(make_tuple(i, j+1));
					//printf("Update for [%d][%d]\n", i, j+1);
				}
			}
			if (j > 0 && grid[i][j-1] > 0 ) {
				if (grid[i][j] < INT_MAX - 1 && grid[i][j-1] > grid[i][j] + 1) {
					grid[i][j-1] = grid[i][j] + 1;
					q.push(make_tuple(i, j-1));
					//printf("Update for [%d][%d]\n", i, j-1);
				}
			}
		}
	}
};

int main() {
	Solution sol;
	vector<vector<int> > rooms   { {INT_MAX, -1, 0, INT_MAX},
								  {INT_MAX, INT_MAX, INT_MAX, -1},
								  {INT_MAX, -1, INT_MAX, -1},
								  {0, -1, INT_MAX, INT_MAX} };	
	sol.wallsAndGates(rooms);
	int i, j;
	for ( i = 0; i < rooms.size(); i++) {
		for ( j = 0; j < rooms[i].size(); j++) {
			printf("%d		", rooms[i][j]);
		}
		printf("\n");
	}

}
