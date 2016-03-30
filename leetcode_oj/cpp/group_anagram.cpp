/*
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case
*/
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<string> > groupAnagrams(vector<string>& strs) {
		unordered_map <string, vector<string> > map;
		for (vector<string>::iterator i = strs.begin(); i != strs.end(); i++) {
			string s(*i);
			sort(s.begin(), s.end());
			map[s].push_back(*i);
		}
		vector<vector<string> > res;
		for (unordered_map <string, vector<string> >::iterator iter = map.begin(); iter != map.end(); ++iter) {
			vector<string> ana(iter->second.begin(), iter->second.end());
			sort(ana.begin(), ana.end());
			res.push_back(ana);
		}
		return res;
    }
};
int main() {
	string a[] = {"eat", "tea", "tan", "ate", "nat", "bat"};
	vector<string> v;
	v.assign(a, a+ (sizeof(a)/sizeof(a[0]))); 
	Solution sol;
	vector<vector<string> > res = sol.groupAnagrams(v);
	for (vector<vector<string> >::iterator i1 = res.begin(); i1 != res.end(); i1++) {
		for(vector<string>::iterator iter=i1->begin(); iter != i1->end(); iter++) {
			cout << *iter << ", ";
		}
		cout << endl;
	}
}
