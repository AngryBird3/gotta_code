/*
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
*/
#include <iostream>
#include <stdio.h>
#include <deque>
#include <vector>
#include <unordered_map>
using namespace std;
class Solution {
public:
    string minWindow(string s, string t) {
		unordered_map <char, deque<int> > indices;
		vector<char> remaining;
		remaining.reserve(t.size());
		vector<char>::iterator it; 

		int maxm, minm;

		for(int i = 0; i < t.size(); i++) {
			indices[t[i]] = deque<int>(); //Store indices of each char, why? substr char might repeat e.g. AAC, we need two A	
			remaining.push_back(t[i]);
		} 

		int start = 0;
		int end = s.size();
	
		for(int i = 0; i < s.size(); i++) {
			//printf("\n--------\n");
			//printf("%c %s\n", s[i], s.substr(start, end+1).c_str());

			/*debugging
			for (std::vector<char>::const_iterator i = remaining.begin(); i != remaining.end(); ++i)
    			std::cout << *i << ' ';
			//debugging end */

			if(indices.find(s[i]) != indices.end()) {
				if(find(remaining.begin(), remaining.end(), s[i]) == remaining.end() && indices[s[i]].size() > 0) {
					printf("poping\n");
					indices[s[i]].pop_front();
				} else {
					it = find(remaining.begin(), remaining.end(), s[i]);
					if(it != remaining.end()) {
						remaining.erase(it);		
					}
				}
				indices[s[i]].push_back(i);
			}
			if(remaining.size() == 0) {
				//std::vector<Val> vals;
				//vals.reserve(indices.size());
				maxm = INT_MIN;
				minm = INT_MAX;
				for(std::unordered_map<char,deque<int> >::iterator iter = indices.begin(); iter != indices.end(); ++iter)
				{
					deque<int> val = iter->second;
					//vals.push_back(kv.second);  
					maxm = max(val.back(), maxm);
					minm = min(val.front(), minm);
				} 
				if (maxm - minm + 1 < end - start +1) {
					start = minm;
					end = maxm;
				}
			}	
		}	
		if (remaining.size() != 0)
			return string();
		return s.substr(start, end+1);
    }
};

int main() {
	Solution sol = Solution();
	string s("ADOBECODEBANC");
	string t("ABC");
	cout << sol.minWindow(s, t) << endl;	
	return 0;
}
