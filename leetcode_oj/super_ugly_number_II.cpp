/*
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

Show Company Tags
Show Tags
Hide Similar Problems
*/
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
		/*
		 * Algorithm
			Just like ugly numbers - II:
			1) next # would be multiplying prime with result
			2) Find minimum
			3) Increment index of that prime

		ugly = [1] 
        i2, i3, i5 = 0, 0, 0
        for i in range(n-1):
            u2, u3, u5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
            umin = min((u2, u3, u5))
            if umin == u2: 
                i2 += 1
            if umin == u3: 
                i3 += 1
            if umin == u5: 
                i5 += 1
            ugly.append(umin)
        return ugly[-1]
			
		 */
 		vector<int> res(n, 0);
		res[0] = 1;
		vector<int> idx(primes.size(), 0);
		for (int i = 1; i < n; i++) {
			res[i] = INT_MAX
			for (int j = 0; j < primes.size(); j++) {
				res[i] = min(res[i], primes[j] * res[idx[j]]);
			}
			for (int j = 0; j < primes.size(); j++) {
				if (res[i] == primes[j] * res[idx[j]]) {
					idx[j]++;
				}
			}
		}       
		return res[n-1];
    }
};
