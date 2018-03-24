#include <iostream>

using namespace std; //Don’t use it!

class Box {
   public:
      double length;   // Length of a box
      double breadth;  // Breadth of a box
      double height;   // Height of a box

   Box(int length, int breadth, int height) : length(length), breadth(breadth), height(height) { cout << "Hi Dhara!" << "\n";}

   string get_key(string s) {
        string res;
        for (auto &c : s) {
            if (c < s[0]) {
                res = res + to_string((c - s[0])%26 + 26) + "-";
            } else {
                res = res + to_string((c - s[0])%26) + "-";
            }
        }
        cout << "res: " << res << "\n";
        return res;
   }
};

int main() {
    //Box box(1,2,3);
    //Box *box = new Box(1,2,3);
    //shared_ptr<Box> shared_box = make_shared<Box>(1,2,3);
    auto shared_box = make_shared<Box>(1,2,3);
    string res = shared_box->get_key("az") ;
    shared_box->get_key("ba") ;
    return 0;
}
