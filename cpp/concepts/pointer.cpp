#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int a = 1;
	int *pa;
	int **ppa = &pa; 
	*ppa = &a; //Both ppa and pa are pointing to a
	cout << **ppa << " " << *pa << endl;
	*pa = 5;
	cout << **ppa << " " << *pa << endl;
	return 0;
}

