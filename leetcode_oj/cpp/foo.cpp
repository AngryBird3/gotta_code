#include <iostream>
#include <cassert>

class Foo
{
public:
  Foo () = default;
  //
  // Foo (const Foo &cf) {
  //   std::cout << "I am at copy-const" << std::endl;
  // }

  Foo (Foo &&mv) {
    std::cout << "I am at move-const" << std::endl;
  }

  Foo& operator=(const Foo &cf) {
    std::cout << "I am at assignment-operator" << std::endl;

    return *this;
  }


};

Foo bar() {
  return Foo();
}

int main() {
  // Compilation error
  // Foo &f = bar();

  // Valid for read-only no constructor will be called
  // const Foo &f1 = bar();

  // assignment-operator
  Foo f3(bar());

  Foo f4;
  f4 = f3;


  // copy-const
 //Foo f5(f4);

  // C++11: using lvalue reference, and using the temp memory
  // Foo &&f4 = bar();
}
