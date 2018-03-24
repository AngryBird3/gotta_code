#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

vector<string> split(const string &s, char delim) {
  vector<string> elems;
  stringstream ss(s);
  string item;
  while (getline(ss, item, delim)) {
    elems.push_back(item);
  }
  return elems;
}

string join(const vector<string>& input) {
  string output = "";
  bool has_data = false;
  for (size_t i = 0; i < input.size(); ++i) {
    has_data = true;
    output += input[i];
    output += ", ";
  }
  if (has_data) {
    output = output.substr(0, output.length() - 2);
  }
  return output;
}

class FileSystem {
 public:
  vector<string> Ls(const string& path) {
    // IMPLEMENT ME
    vector<string> output;
    return output;
  }

  void MkdirP(const string& dir_path) {
    // IMPLEMENT ME
  }

  void AddFileWithContent(const string& file_path, const string& content) {
    // IMPLEMENT ME
  }

  string GetFileContent(const string& file_path) {
    // IMPLEMENT ME
    return "";
  }
};


#ifndef __main__
#define __main__

int main(int argc, char* argv[]) {
  FileSystem fs;

  // should print ""
  cout << join(fs.Ls("/")) << endl;
  fs.MkdirP("/a/b/c");
  fs.AddFileWithContent("/a/b/c/d", "hello world");
  // should print a
  cout << join(fs.Ls("/")) << endl;
  // should print d
  cout << join(fs.Ls("/a/b/c")) << endl;
  // should print d
  cout << join(fs.Ls("/a/b/c/d")) << endl;
  // should print hello world
  cout << fs.GetFileContent("/a/b/c/d") << endl;
}

#endif


