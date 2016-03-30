/*
Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
*/
#include <stdio.h>
#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    vector<string> generateAbbreviations(string word) {
 		/*
		 *  Algo:
		 *  
		 *  rec(string, start , set_abbr, word):
		 *	
		 *
		 *		rec(word, i+1)
		 *		for i in range(start, word):
		 *			At each index either keep it or abbreiveit with # of char
		 *				
		 *			a) 
		 *			rec('i' + word[i+1:], i+2)
		 *			Q: How to make sure I don't do this: 12d :i+2	
		 */     

		vector<string> res;
		rec(word, 0, "", res);

		return res;

	}

	void rec(string word, int start, string tmp, vector<string> &res) {
		if (start >= word.length()) {
			//printf("word: %s\n", word.c_str());
			res.push_back(tmp);
			return;
		}  

		int i;
		//No abbreiviation
		rec(word, start + 1, tmp+word[start], res);
		for( i = start; i < word.length(); i++) {
			//Abbreviation from start to i
			int len = i - start + 1; //Making sure not considering int before
			string next = tmp + to_string(len);
			if (i < word.length() - 1)
				next += word[i+1];
			//printf("i: %d start: %d tmp: %s next: %s\n", i, start, tmp.c_str(), next.c_str());
			rec(word, i + 2, next, res);
		}
    }
};

int main() {
	string w = "word";
	Solution s;
	vector<string> res = s.generateAbbreviations(w);
	for(vector<string>::iterator itr = res.begin();
		itr < res.end(); itr++) {
		printf("%s, ", itr->c_str());
	}
	printf("\n");
}
