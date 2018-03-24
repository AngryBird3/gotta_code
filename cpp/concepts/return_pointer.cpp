#include <iostream>

class Foo { 
public:
    Foo(): a(5) {
        std::cout << "Foo constructor" << "\n";
    }

    Foo(const Foo& rhs) : a(10) {
        std::cout << "Foo copy constructor" << "\n";
    }

    Foo& operator=(const Foo& rhs) {
        std::cout << "Foo assignment operator" << "\n";
        return *this;
    }

    ~Foo() {
        std::cout << "Foo destructor" << "\n";
    }

    int a;
};

const std::shared_ptr<Foo> get_foo() {
    std::cout << "get_foo" << "\n";
    return std::shared_ptr<Foo>(new Foo());
}

int main() {
    //const Foo& f = *get_foo();
    //std::cout << f.a << "\n";

    Foo *f = get_foo().get();
    std::cout << f->a << "\n";

    //std::shared_ptr<Foo> f = get_foo();
    //Foo &f_ref = *f;
    //std::cout << f->a << " count: " << f.use_count() << "\n";
}
