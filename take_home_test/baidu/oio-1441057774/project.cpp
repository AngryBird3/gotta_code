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
	for(int file = 0; file < (int)filenames.size(); file++) {
			vector<vector<int>> opt(pattern.size()+1, vector<int>(filenames[file].size()+1, 0));
			opt[0][0] = true;
			int i,j;
			//Init table
			// 0 length string but we have pattern
			// If our previous' previous true AND current is * (as * can eliminate everything) or ?
			for(i=1; i < (int)pattern.size()+1; i++) {
				opt[i][0] = opt[i-1][0] and (pattern[i - 1] == '*' or pattern[i-1] == '?');
			//	printf("pattern: %c, opt[i][j]: %d\n", pattern[i-1], opt[i][0]);
			}

			for(i=1; i < (int)pattern.size() + 1; i++) {
				//printf("------\n");
				//printf("Pattern i: %c\n", pattern[i-1]);
				for(j=1; j < (int)filenames[file].size() + 1; j++) {
			//		printf("Str j: %c, opt[i-1][j-1]: %d, opt[i][j-1]: %d, opt[i-1][j]: %d\n", filenames[file][j-1], opt[i-1][j-1], opt[i][j-1], opt[i-1][j]);
					// 1) If its NOT *; easy one - update diagonally; if current is same or ? =? true
					if (pattern[i-1] != '*') {
						opt[i][j] = opt[i-1][j-1] and (filenames[file][j-1] == pattern[i-1] or pattern[i-1] == '?');
					} else {
						//2) If its *, i-1 and j match, vertical [i-1][j] or horizontal [i][j-1]
						opt[i][j] = opt[i-1][j] or opt[i][j-1];
					}
			//		printf("opt[i][j]: %d\n", opt[i][j]);
				}
			}
			i = (int)pattern.size();
			j = (int)filenames[file].size();
			if(opt[i][j]) {
				// If it match
			//	printf("It did match\n");
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

int main() {
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
