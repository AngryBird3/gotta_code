#include <iostream>
using namespace std;

class abstractClass {
public:
    abstractClass() {
        cout << "abstractClass" << "\n";
    }
    virtual void implementMe() = 0;
};

class DefaultAbstractClass : public abstractClass{
public:
    DefaultAbstractClass() {
        cout << "DefaultAbstractClass" << "\n";
    }
    void implementMe() {
        cout << "Hi!" << "\n";
    }
};

int main() {
    /* following not going to work: variable type 'abstractClass' is an abstract class
    abstractClass a;
    a.implementMe();
    */
    abstractClass *a = new DefaultAbstractClass();
    a->implementMe();
}
