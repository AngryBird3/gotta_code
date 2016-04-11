/*
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
*/

#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <set>
using namespace std;
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<pair<int, int> >& prerequisites) {
		//vector<vector<int> > graph (numCourses, vector<int>(numCourses, 0));
		unordered_map<int, set<int> > graph;
		vector<int> indegree(numCourses, 0);
        //Create graph and indegree
		for (vector<pair<int, int> >::iterator itr = prerequisites.begin();
					itr != prerequisites.end(); itr++) {
			//graph[itr->second][itr->first] = 1;
			graph[itr->second].insert(itr->first);
			//indegree[itr->first]++;
			cout << "node i: " << itr->first << " indegree: " << indegree[itr->first] << "\n";
		}

		for (unordered_map<int, set<int> >::iterator itr = graph.begin();
						itr != graph.end(); itr++) {
			set<int> n = itr->second;
			for (set<int>::iterator i = n.begin(); i != n.end(); i++) {
				indegree[*i]++;
			}
		}
		//Q
		queue<int> q;
		//Find root with indegree 0
		for(int i = 0; i < numCourses; i++) {
			cout << "node i: " << i << " indegree: " << indegree[i] << "\n";
			if (indegree[i] == 0) {
				q.push(i);
			}	
		}

		//Topological sort
		vector<int> res;
		int count = 0;
		while(!q.empty()) {
			int course = q.front();
			q.pop();
			res.push_back(course);
			count++;
			cout << " course: " << course << " count: " << count << "\n";
			//Decrement indegree of neighbors
			//and add into queue
			//if (graph[course][i]) {
			//if(graph[course].find(i) != graph[course].end()) {
			for (set<int>::iterator itr = graph[course].begin();
						itr != graph[course].end(); itr++) {
				if (--indegree[*itr] == 0) {
					q.push(*itr);
				}
			}
		}
		if (count == numCourses) return res;
		return vector<int>();
    }
};

int main() {
	Solution sol;
	//vector<pair<int, int> > prerequisites {{0,1},{1,2},{2,3},{3,0}};
	vector<pair<int, int> > prerequisites {{5,8},{3,5},{1,9},{4,5},{0,2},{1,9},{7,8},{4,9}};
	vector<int> res = sol.findOrder(10,prerequisites);
	std::copy(res.begin(), res.end(),
            std::ostream_iterator<int>(cout, " "));
	cout << "\n";
	return 0;
}
