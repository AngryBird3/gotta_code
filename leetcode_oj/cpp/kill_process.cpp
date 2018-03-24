/*
Given n processes, each process has a unique PID (process id) and its PPID (parent process id).

Each process only has one parent process, but may have one or more children processes. This is just like a tree structure. Only one process has PPID that is 0, which means this process has no parent process. All the PIDs will be distinct positive integers.

We use two list of integers to represent a list of processes, where the first list contains PID for each process and the second list contains the corresponding PPID.

Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that will be killed in the end. You should assume that when a process is killed, all its children processes will be killed. No order is required for the final answer.

Example 1:
Input:
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
Output: [5,10]
Explanation:
          3
        /   \
       1     5
            /
           10
Kill 5 will also kill 10.
Note:
The given kill id is guaranteed to be one of the given PIDs.
n >= 1.
**/

class Tree {
public:
    int id;
    int parent;
    vector<int> children;
};

class Solution {
public:
    vector<int> killProcess(vector<int>& pid, vector<int>& ppid, int kill) {

        // Create Tree Structure
        unordered_map<int, shared_ptr<Tree> > created_nodes;
        int n = pid.size();
        for (int i = 0; i < n; i++) {
            shared_ptr<Tree> node;
            shared_ptr<Tree> parent_node;
            if (created_nodes.find(pid[i]) == created_nodes.end()) {
                node = make_shared<Tree>();
                created_nodes[pid[i]] = node;
            } else {
                node = created_nodes[pid[i]];
            }
            if (created_nodes.find(ppid[i]) == created_nodes.end()) {
                parent_node = make_shared<Tree>();
                created_nodes[ppid[i]] = parent_node;
            } else {
                parent_node = created_nodes[ppid[i]];
            }
            (parent_node->children).push_back(pid[i]);
            node->parent = ppid[i];
        }

        // Now use Tree
        if (created_nodes.find(kill) == created_nodes.end()) {
            return vector<int>();
        }
        vector<int> result;
        deque<int> q;
        q.push_back(kill);
        result.push_back(kill);
        while (!q.empty()) {
            shared_ptr<Tree> node = created_nodes[q.front()];
            q.pop_front();
            for (auto &child : node->children) {
                q.push_back(child);
                result.push_back(child);
            }
        }
        return result;
    }
};
