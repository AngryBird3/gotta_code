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
		if (n <= 1) {
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

		int count = 1;
		queue.push_back(0);
		visited[0] = 1;
		bool flag = 0;
		while (num_of_visited <= n - 1) {
			if (flag != 0) {
				count++; //More component
				//Find the first node which isn't visited from the visited vector
				int node = distance(visited.begin(),
								find(visited.begin(), visited.end(), 0));
				queue.push_back(node);	
				printf("node: %d, count: %d, num_of_visited: %d\n", node, count,
										num_of_visited);
			}
			while (!queue.empty()) {
				int node = queue.front();	
				queue.pop_front();
				num_of_visited++;

				//Get neighbours
				for(vector<int>::iterator it=adj_list[node].begin();
					it < adj_list[node].end(); it++) {
					//printf("Neighbor: %d\n", *it);
					if(!visited[*it]) {
						visited[*it] = 1;	
						queue.push_back(*it);
					}
				}
			}	
			flag = 1;
			printf("# of visited: %d\n", num_of_visited);
		}

		return count;
    }
};

int main() {
	Solution s;
	vector<pair<int, int> > edges;
	//Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.
	//[[0,1],[1,2],[2,3],[3,4]]
	edges.push_back(make_pair(0, 1));
	edges.push_back(make_pair(1, 2));
	//edges.push_back(make_pair(2, 3));
	edges.push_back(make_pair(3, 4));
	
	//vector<pair<int, int> > ed1;
	int components = s.countComponents(5, edges); 
	printf("# of components: %d\n", components);
}	
