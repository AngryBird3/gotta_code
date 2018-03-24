#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Glob {
 public:
  vector<string> Match(const string& pattern, const vector<string>& filenames) const {
    // IMPLEMENT ME
    vector<string> output;

	// DP table of n+1 x m+1
	for(int file = 0; file < filenames.size(); file++) {
			vector<vector<bool>> opt(pattern.size()+1, vector<bool>(filenames[file].size()+1, false));

			opt[0][0] = true;
			//Init table
			// 0 length string but we have pattern
			// If our previous' previous true AND current is * (as * can eliminate everything)
			for(int i=2; i <pattern.size()+1; i++) {
				opt[i][0] = opt[i-2][0] and (strcmp(pattern[i - 1].c_str(),"*")==0);
			}

			for(int i=0; i < pattern.size() + 1; i++) {
				for(int j=0; j < filenames[file].size() + 1; j++) {
					// 1) If its NOT *; easy one - update diagonally; if current is same or ? =? true
					opt[i][j] = opt[i-1][j-1] and (strcmp(filenames[file][j], pattern[i]) == 0 or strcmp(pattern[i], "?") == 0);
				
					//2) If its *, this is difficult. Either pattern :i-2 and string :j match or :i-1 and j match
					opt[i][j] = opt[i-2][j] or opt[i-1][j];
				}
			}
			if(opt[i][j]) {
				// If it match
				output.push_back(filenames[file]);
			}
	}
    return output;
  }
};

bool vector_equal(const vector<string>& expected, const vector<string>& actual) {
  if (expected.size() != actual.size()) {
    return false;
  }
  for (size_t i = 0; i < expected.size(); ++i) {
    if (expected[i] != actual[i]) {
      return false;
    }
  }
  return true;
}

#ifndef __main__
#define __main__

int main(int argc, char* argv[]) {
  // Should return true
  cout << vector_equal(
      { "abcd", "dabc", "abc" },
      Glob().Match("?abc*", { "abcd", "dabc", "abc", "efabc", "eadd" })) << endl;
  // Should return true
  cout << vector_equal(
      { "abcd", "dabc", "abc" },
      Glob().Match("?a**c*", { "abcd", "dabc", "abc", "efabc", "eadd" })) << endl;
}

#endif
