#include <iostream>

int main() {
  int &&a = 5;
  //std::cout << &a << std::endl;
  int b = 10;
  int &b_ref = b;
  int *b_ptr = &b_ref;
  (*b_ptr)++;


  int **c = &b_ptr;
  **c = 20;

  std::cout << b_ref << " " << b << std::endl;
}
