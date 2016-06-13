/*
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

For example,
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Note:
You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
Hide Company Tags Google Airbnb Facebook Twitter Snapchat Pocket Gems
Hide Tags Graph Topological Sort
Hide Similar Problems (M) Course Schedule II
Difficulty: Hard
*/
class Solution {
public:
    unordered_map<char, set<char> > graph;

    void create_graph(vector<string>& words, unordered_map<char, int>& indegree) {
        //Create 0 indegree for all uniq letters
        for (int i = 0; i < words.size(); i++) {
            for (int j = 0; j < words[i].length(); j++) {
                indegree[words[i][j]] = 0;
            }
        }
        //Go through words pair, and when the char mismatch
        //create an edge between i to i+1
        for (int i = 0; i < words.size()-1; i++) {
            string a1 = words[i];
            string a2 = words[i+1];
            int j = 0;
            int len = min(a1.length(), a2.length());
            while (j < len) {
                if(a1[j] != a2[j]) {
                    //Mismatch, create edge from a1[j] to a2[j]
                    if (graph[a1[j]].find(a2[j]) == graph[a1[j]].end()) {
                        graph[a1[j]].insert(a2[j]);
                        indegree[a2[j]] += 1;
                    }   
                    break;
                }   
                j++;
            }   
        }   
    } 

    string alienOrder(vector<string>& words) {
        unordered_map<char, int> indegree;
        //Create graph, and get indegree
        create_graph(words, indegree);

        //Do topological sort
        queue<char> q;

        //Find the node with 0 indegree
        for (unordered_map<char, int>::iterator itr = indegree.begin();
                            itr != indegree.end(); itr++) {
            //cout << "indegree[" << itr->first << "]: " << itr->second << "\n";
            if (itr->second == 0) {
                q.push(itr->first);
            }
        }

        //order
        string res = "";
        while(!q.empty()) {
            char node = q.front();
            q.pop();
            res += node;

            //Neighbors, and indegree
            for(set<char>::iterator itr = graph[node].begin();
                        itr != graph[node].end(); itr++) {
                if(--indegree[*itr] == 0) {
                    q.push(*itr);
                }
            }
        }
        if (res.length() != indegree.size()) return "";
        return res;
    }
};
