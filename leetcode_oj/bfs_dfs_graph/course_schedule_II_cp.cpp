#include <iostream>
#include <vector>
#include <unordered_set>
#include <queue>
using namespace std;
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<unordered_set<int>> graph = make_graph(numCourses, prerequisites);
        vector<int> degrees = compute_indegree(graph);
        queue<int> zeros;
        for (int i = 0; i < numCourses; i++)
            if (!degrees[i]) zeros.push(i);
        vector<int> toposort;
        for (int i = 0; i < numCourses; i++) {
            if (zeros.empty()) return {};
            int zero = zeros.front();
            zeros.pop();
            toposort.push_back(zero);
            for (int neigh : graph[zero]) {
                if (!--degrees[neigh])
                    zeros.push(neigh);
            }
        }
        return toposort;
    }
private:
    vector<unordered_set<int>> make_graph(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<unordered_set<int>> graph(numCourses);
        for (auto pre : prerequisites)
            graph[pre.second].insert(pre.first);
        return graph; 
    }
    vector<int> compute_indegree(vector<unordered_set<int>>& graph) {
        vector<int> degrees(graph.size(), 0);
        for (auto neighbors : graph)
            for (int neigh : neighbors)
                degrees[neigh]++;
        return degrees;
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
