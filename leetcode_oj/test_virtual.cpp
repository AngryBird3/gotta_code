#include <stdio.h>

class foo {
 public:
	foo() {
		printf("Inside foo constructor...\n");
	}
};
class bar : public foo {
 public:
	bar() {
		printf("Inside bar constrctor ...\n");
	}
};

int main() {
	foo *p = new bar();
	return 0;
}
