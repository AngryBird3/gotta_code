/*
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Credits:
Special thanks to @minglotus6 for adding this problem and creating all test cases.

Hide Company Tags Dropbox Uber
Hide Tags Hash Table
Hide Similar Problems (E) Isomorphic Strings (H) Word Pattern II
Difficulty: Easy
*/
class Solution {
public:
    bool wordPattern(string pattern, string str) {
        /*
         * Algorithm:
         * ith char in pattern is ith word in string
         * they both should always match
         * a) break string into words
         * b) Store ith char in hash as key if its not present
         * with value as ith word
         *     if its there in hash and doesn't match with
         *      ith word in str , return False
         */
         
         //Base case: If both of them are empty
         if (!str.length() && !pattern.length()) {
             return true;
         } 
         //Base case: If only one of them are empty
         if (!str.length() || !pattern.length()) {
             return false;
         }
         
         unordered_map<char, string> hash_p;
         unordered_map<string, char> hash_v;
         
         int i = 0; //For pattern [i]
         
         istringstream iss(str); //For word break
         string word;
         while(iss >> word) {
            /* do stuff with word */
            //printf("i: %d, pattern len: %d\n", i, pattern.length());
            if (i >= pattern.length()) {
                //I still have word but no pattern
                return false;
            }
            // b)
            unordered_map<char, string>::const_iterator got_p = hash_p.find(pattern[i]);
            unordered_map<string, char>::const_iterator got_v = hash_v.find(word);
            if ( got_p == hash_p.end() && got_v == hash_v.end()) {
                //Pattern/value not there, add into hash
                hash_p[pattern[i]] = word;
                hash_v[word] = pattern[i];
            } else if (got_p != hash_p.end()) {
                //If pattern's there
                if (got_p->second != word) return false;
            } else if (got_v != hash_v.end()) {
                //If value's there
                if (got_v->second != pattern[i]) return false;
            }
        
            i++;
         }
         
        return i == pattern.length();
    }
};
