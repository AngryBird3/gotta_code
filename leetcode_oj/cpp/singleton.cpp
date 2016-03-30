#include <iostream>
class singleton {
	private:
		singleton() { }
		static singleton *s;
	public:
		static singleton* get_obj() {
			if (!s) {
				s = new singleton();
			}
			return s;
		}
};

singleton* singleton::s = NULL;
int main() {
	singleton* my_s = singleton::get_obj();
}
