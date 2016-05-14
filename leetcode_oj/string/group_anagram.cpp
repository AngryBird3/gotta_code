/*
Total Accepted: 74938 Total Submissions: 271336 Difficulty: Medium
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
All inputs will be in lower-case.
Hide Company Tags Amazon Bloomberg Uber Facebook Yelp
Hide Tags Hash Table String
Hide Similar Problems (E) Valid Anagram (E) Group Shifted Strings
*/
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
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
