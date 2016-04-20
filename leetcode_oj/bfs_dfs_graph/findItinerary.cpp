/*
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
*/
#include <stdio.h>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <set>
using namespace std;
class Solution {
	unordered_map<string, set<string> > graph; //multiset, as edge repeats
public:
    vector<string> findItinerary(vector<pair<string, string> > tickets) {
    	// Create graph
		for (vector<pair<string, string> >::iterator itr = tickets.begin();
					itr != tickets.end(); itr++) {
			graph[itr->first].insert(itr->second);
		} 

		//Find path
		vector<string> res;
		dfs("JFK", res);
		return vector<string>(res.rbegin(), res.rend());
    }

	void dfs(string u, vector<string> &path) {
		cout << "U: " << u << "\n";
		while(graph[u].size()) {
			// Get the first neighbor node v (lexi 1st)
			string v = *graph[u].begin();
			//Mark it visited
			graph[u].erase(graph[u].begin());
			//recurse!
			cout << "V: " << v << "\n";
			dfs(v, path);
		}
		cout << "pushing " << u << "\n";
		path.push_back(u);
	}
};

int main() {
	Solution sol;
	//vector<pair<string, string> > tickets {{"MUC", "LHR"}, {"JFK", "MUC"}, {"SFO", "SJC"}, {"LHR", "SFO"}};
	//vector<pair<string, string> > tickets {{"A", "C"} , {"C", "D"}, {"D", "A"}, {"D", "B"}, {"JFK", "A"}, {"JFK", "D"}, {"B", "C"}};
	vector<pair<string, string>> tickets {{"EZE","AXA"},
			{"TIA","ANU"},{"ANU","JFK"},{"JFK","ANU"},
			{"ANU","EZE"},{"TIA","ANU"},{"AXA","TIA"},
			 {"TIA","JFK"},{"ANU","TIA"},{"JFK","TIA"}};
/*
AXA: TIA, 
TIA: ANU, JFK, 
EZE: AXA, 
ANU: EZE, JFK, TIA, 
JFK: ANU, TIA, 
*/
	vector<string> path = sol.findItinerary(tickets);
	for (auto i = path.begin(); i != path.end(); ++i)
    	std::cout << *i << ' ';
	cout << "\n";
	return 0;
}
