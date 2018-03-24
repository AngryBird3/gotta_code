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
			vector<vector<bool>> opt(pattern.size()+1, vector<bool>(filenames[file].size()+1, false);

			opt[0][0] = true;
			//Init table
			// 0 length string
			for(int i=2; i <pattern.size()+1; i++) {
				opt[i][0] = 
			}

			for(int i=0; i < pattern.size() + 1; i++) {
				for(int j=0; j < pattern.size() + 1; j++) {

					
				}
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
