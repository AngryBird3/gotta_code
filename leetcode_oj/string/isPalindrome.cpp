'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

Hide Company Tags Microsoft Uber Facebook Zenefits
Hide Tags Two Pointers String
Hide Similar Problems (E) Palindrome Linked List
Difficulty: Easy
'''
class Solution {
public:
    bool isPalindrome(string s) {
        size_t len = s.length();
        int start = 0, end = len;
        while (start < end) {
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
};
