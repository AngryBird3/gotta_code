#include <stdio.h>
#include <iostream>
using namespace std;
class Solution {
public:
    void reverseWords(string &s) {
        int n = s.length() - 1;
        reverse(s, 0, n);
        int i, start = 0;
        for (i = 0; i < n; i++) {
            if (isspace(s[i])) {
                reverse(s, start, i-1);
                start = i+1;
            }
        } 
		reverse(s, start, n);
    }
    
    void reverse(string &s, int start, int end) {
        int i, j;
        char temp;
        for (i = start, j = end; i < j; i++, j--) {
            temp = s[i];
            s[i] = s[j];
            s[j] = temp;
        }
    }
};

int main() {
	Solution s;
	//string str("the sky is blue");
	string str("a b");
	s.reverseWords(str);
	printf("Revsersed string : %s\n", str.c_str());
	return 0;
}
