/*
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
*/
#include <stdio.h>
#include <string>
using namespace std;
class Solution {
public:
    bool isPalindrome(string s) {
		size_t len = s.length();
		int start = 0, end = len-1;
		while (start < end) {
			printf("[DEBUG] start: %c, end: %c\n", s[start], s[end]); 
			if(!isalnum(s[start])) {
				start++;
				continue;
			}
			if(!isalnum(s[end])) {
				end--;
				continue;
			}
			if(tolower(s[start]) != tolower(s[end])) {
				return false;
			}
			start++; end--;
		}	       
		return true;
    }
	bool isPalindrome2(string s) {
		int start, end;
        for (start = 0, end = s.length(); start < end; start++, end--) {
            while(!isalnum(s[start])) 
                start++;
            while(!isalnum(s[end])) 
                end--;
            if (tolower(s[start]) != tolower(s[end]) )
                return false;
        }
        return true;
	}
};

int main()
{
	Solution s;
	printf("%d\n", s.isPalindrome2("   "));
	return 0;
}
