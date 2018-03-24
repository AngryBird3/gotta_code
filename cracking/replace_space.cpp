#include <stdio.h>
#include <iostream>
using namespace std;

void replace_space(string &s) {
	int num_of_space = 0;
	for (int i = 0; i < s.length(); i++) {
		if (isspace(s[i]))
			num_of_space++;
	}
	//printf("Num_of_space: %d\n", num_of_space);
	int l = s.length();
	s.resize(l + (2 * num_of_space));
	//printf("s new size: %lu, old length: %d\n", s.length(), l);
	for (int i = s.length(); i >= 0; i--, l--) {
		//printf("l: %d\n", l);
		if (isspace(s[l])) {
			//printf("space l: %d\n", l);
			s[i--] = '0';
			s[i--] = '2';
			s[i] = '%';	
		} else {
			s[i] = s[l];
		}
	}
}

int main() {
	string s = "a b cd";
	replace_space(s);
	printf("%s\n", s.c_str());

	s = "  ";
	replace_space(s);
	printf("%s\n", s.c_str());

	s = "ab ";
	replace_space(s);
	printf("%s\n", s.c_str());
	
	s = "a";
	replace_space(s);
	printf("%s\n", s.c_str());
}
