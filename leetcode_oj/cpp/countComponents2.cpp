/*
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
*/
#include <iostream>
#include <stdio.h>
#include <vector>
#include <deque>
#include <unordered_map>
#include <algorithm>

using namespace std;
class Solution {
public:
    int countComponents(int n, vector<pair<int, int> >& edges) {
		if (n < 1) {
			return 1;
		}
    	unordered_map<int, vector<int> > adj_list;
		deque<int> queue;
		vector<int> visited(n, 0);
		int num_of_visited = 0;

		//Create adjacency list
		for(vector<pair<int,int> >::iterator it=edges.begin();
								it < edges.end(); it++) {
			if (adj_list.find(it->first) == adj_list.end()) {
				adj_list[it->first] = vector<int>();
			}
			adj_list[it->first].push_back(it->second);
			if (adj_list.find(it->second) == adj_list.end()) {
				adj_list[it->second] = vector<int>();
			}
			adj_list[it->second].push_back(it->first);
		} 
		int count = 0;
		for (int i = 0; i < n; i++) {
			if(!visited[i]) {
				count++;
				dfs(i, visited, adj_list);
			}
		}
		return count;
    }
	void dfs(int i, vector<int>& visited, 
			unordered_map<int, vector<int> >& adj_list) {
		if(visited[i])	return;
		visited[i] = 1;
		for(int j = 0; j < adj_list[i].size(); j++) {
			dfs(adj_list[i][j], visited, adj_list);
		}
	} 
};

int main() {
	Solution s;
	vector<pair<int, int> > edges;
	//Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.
	// 5 [[0,1],[1,2],[2,3],[3,4]]
	edges.push_back(make_pair(0, 1));
	edges.push_back(make_pair(1, 2));
	edges.push_back(make_pair(2, 3));
	edges.push_back(make_pair(3, 4));
	
	//vector<pair<int, int> > ed1;
	int components = s.countComponents(6, edges); 
	printf("# of components: %d\n", components);
}	
