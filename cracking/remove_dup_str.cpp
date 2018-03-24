#include <stdio.h>
#include <iostream>
using namespace std;

void remove_dup(string &s) {
	//Sort it
	// abccdabr -> aabbccdr
	sort(s.begin(), s.end());

	//If its same as previous char
	//Ignore copying
	int new_str_end = 0;
	for (int i = 0; i < s.length(); i++) {
		if(s[i] == s[i - 1]) {
			continue;
		}
		s[new_str_end] = s[i];
		new_str_end++;
	}
	while(new_str_end < s.length()) {
		s[new_str_end] = '\0';
		new_str_end++;
	}
}

int main() {
	string s1 = "";
	remove_dup(s1);
	string s2 = "abccdabr";
	remove_dup(s2);
	string s3 = "aaaaaa";
	remove_dup(s3);
	string s4 = "abcd";
	remove_dup(s4);
	printf("%s\n%s\n%s\n%s\n", s1.c_str(), s2.c_str(), s3.c_str(), s4.c_str());
}
