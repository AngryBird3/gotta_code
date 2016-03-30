/*
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example: 
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
*/
#include <stdio.h>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;
class ValidWordAbbr {
	unordered_map<string, string> abbr;	
	
	string get_abbr(string s) {
		string l = s.length() - 2 > 0 ? to_string(s.length() - 2) : "";
		string abr = s[0] + l + s[s.length() - 1];
		return abr;
	}
public:
    ValidWordAbbr(vector<string> &dictionary) {
    	for (vector<string>::iterator itr=dictionary.begin();
				itr != dictionary.end();
				itr++) {
			string abr = get_abbr(*itr);
			/*
			if (itr->compare("cake") == 0) {
				printf("Abbr: %s\n", abr.c_str());
			}
			*/
			if (abbr.find(abr) != abbr.end()) {
				//Find if there's "OTHER" word with same abbreviation, then "" value
				if (itr->compare(abbr[abr]) != 0) {
					abbr[abr] = "0";
				}
			} else {
				abbr[abr] = *itr;
			}
		} 
    }

    bool isUnique(string word) {
    	string abr = get_abbr(word);
		/*
		if (word.compare("cane") == 0) {
			printf("Abbr of cane: %s\n", abr.c_str());
			printf("word: %s\n", abbr[abr].c_str());
		}
		*/
		if (abbr.find(abr) == abbr.end()) {
			return true;
		}
		if (abbr[abr].compare("0") != 0) {
			//Make sure word == abbr[abr]	
			if (word.compare(abbr[abr]) == 0) {
				return true;
			}
		} 
		return false;
    }
};


// Your ValidWordAbbr object will be instantiated and called as such:
// ValidWordAbbr vwa(dictionary);
// vwa.isUnique("hello");
// vwa.isUnique("anotherWord");

int main() {
	static const string dic[] = {"deer", "door", "cake", "card"};
	vector<string> dictionary(dic, dic + sizeof(dic)/sizeof(dic[0]));
	ValidWordAbbr vwa(dictionary);
	printf("%d\n", vwa.isUnique("dear"));
	printf("%d\n", vwa.isUnique("cart"));
	printf("%d\n", vwa.isUnique("cane"));
	printf("%d\n", vwa.isUnique("make"));
}
