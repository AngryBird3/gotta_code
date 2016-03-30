#include <iostream>
#include <stdio.h>
using namespace std;
void foo();
int main() {
	foo();
	return 0;
}

void foo() {
 int a = 10;
 if (true) { int b = 20; cout << &b << " " << &a << endl;}
 int c = 30;
 cout << &a << "  " << &c << endl;
}
