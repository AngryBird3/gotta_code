#include <math.h>
#include <vector>
#include <iostream>

int CountProgram(int length) {
    std::vector<long long> opt(std::max(length, 2), 0);
    opt[0] = 1;
    opt[1] = 6;
    for (int i = 2; i < length+1; i++) {
        opt[i] = opt[i-1] * 6;
        for(int j = 1; j < i; j++) {
            long long left = opt[j-1];
            long long right = opt[i-j-1];
            opt[i] += (left * right) ;
        }
    }
    return opt[length]% (long)(pow(10, 9) + 7);
}

// Driver program to test above functions
int main()
{
    int n = 15;
    std::cout << CountProgram(n) << "\n";
    return 0;
}
