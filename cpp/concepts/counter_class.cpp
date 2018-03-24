#include <iostream>
using namespace std;

// see below for a discussion of why
// this isn't quite right
 
class Counter {  
public:          
    Counter() { ++count; cout << "Counter constructor\n"; }
    Counter(const Counter&) { ++count; cout << "Counter copy constructor\n"; }
    ~Counter() { --count; }
    static size_t howMany()
        { return count; }
 
private:
    static size_t count;
};
// This still goes in an
// implementation file
size_t Counter::count = 0;

// inherit from Counter to count objects
class Widget: public Counter {
public:
	Widget() { cout << "Widget constructor\n"; }
};
int main() {
	Widget w;
	cout << "w count: " << w.howMany() << "\n";
	return 0;
}
