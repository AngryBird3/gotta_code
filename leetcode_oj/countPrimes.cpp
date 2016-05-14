class Solution {
public:
    int countPrimes(int n) {
        vector<bool> isprimes(max(n,2), true);
        isprimes[0] = false; isprimes[1] = false;
        int x = 2;
        while (x * x < n) {
            if (isprimes[x]) {
                int p = x * x;
                while (p < n) {
                    isprimes[p] = false;
                    p += x;
                }
            }
            x += 1;
        }
        return count_if(isprimes.begin(), isprimes.end(), [](bool i){return i==true;});
    }
};
