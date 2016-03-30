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
		int begin = 0, end = 0;
		int counter = t.size();
		int d = INT_MAX; // Min lengh (d=end -begin)
		int head = 0;

		vector<int> map(128, 0);
		for(int i = 0; i < t.size(); i++) {
			map[t[i]]++;
		}
		
		while(end < s.size()) {
			// if current char (s[end]) in T; decreament remaining
			if(map[s[end++]]-- > 0){
				counter--;
			}
			while(counter == 0) {
				// we've found all the char of T, set max begin/end
				if(end - begin < d) {
					head = begin;
					d = end - begin;
				}
				// Move 'begin' pointer
				// Adjust counter
				if (map[s[begin++]]++ == 0) {
					counter++;
				}
			}
		}
		return d==INT_MAX? "":s.substr(head, d);
	}
};

int main() {
	Solution sol = Solution();
	string s("ADOBECODEBANC");
	string t("ABC");
	cout << sol.minWindow(s, t) << endl;	
	return 0;
}
