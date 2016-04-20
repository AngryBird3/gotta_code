#include <iostream>
#include <unordered_map>
using namespace std;
class Solution {
public:
    string fractionToDecimal(int n, int d) {
    	/*
		 * Algorithm:
		 * Divide like how you literrary do!
		 */ 
		int64_t numerator = n;
		int64_t denominator = d;
		string res;
		if (numerator * denominator < 0) {
			res += "-";
		}
        numerator = abs(numerator);
        denominator = abs(denominator);
		res += to_string(abs(numerator/denominator));
		if (numerator % denominator == 0) return res;
		res += ".";
		long rem = abs(numerator % denominator);
	
		// If numerator(reminder too) has been met before, circulation happens,
		// STOP the computation then return the result.

		//Store numerator and its position we saw last
		//time so that we can replace with ()
		unordered_map<int, int> m;
		while (rem) {
			//Reminder/numerator's current position
			m[rem] = res.size();
			//cout << "rem: " << rem << " m[rem]: " << m[rem] << "\n";
			rem *= 10;
			res += to_string(rem /long(denominator));
			rem = rem % denominator;
			
			if (m.find(rem) != m.end()) {
				res.insert(m[rem], "("); // Replace with ( num )
				res += ")";
				break;
			}		
		}	
		return res;
    }
};

int main() {
	Solution sol;
	cout << sol.fractionToDecimal(2, 3) << "\n";
	return 0;
}
