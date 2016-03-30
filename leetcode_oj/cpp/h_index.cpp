/*
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Hint:

An easy approach is to sort the array first.
What are the possible values of h-index?
A faster approach is to use extra space.
*/
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int hIndex(vector<int>& citations) {
		if (citations.empty()) {
			return 0;
		}
 		/* Approach 1: sort */       
		/*
		sort(citations.begin(), citations.end());
		int hi = 0;
		for(int i = 1; i < citations.size(); i++){
			if (citations[i-1] >= i)
				return i;
			hi = i;
		}	
		return hi;
		*/

		//Approach 2: Hash
		int map[citations.size()+1];
		memset(map, 0, sizeof(map));
		for(int i = 0; i < citations.size(); i++) { 
			if(citations[i] >= citations.size()) {
				map[citations.size()] += 1;
			} else {
				map[citations[i]] += 1;
			}
		}
	
		int h = 0; //accepted citations ;.
		for(int i = citations.size(); i >= 0; --i) {
			h += map[i];
			if (h >= i)
				return i;
		}
		return -1;	
    }
};

int main() {
	Solution sol;
	int a[] = {3, 0, 6, 1, 5};
	vector<int> b(a, a+sizeof(a)/sizeof(a[0]));
	cout << sol.hIndex(b) << endl;
} 
