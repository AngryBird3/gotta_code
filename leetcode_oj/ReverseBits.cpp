class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        for (int i =0; i < 32; i++, n>>=1) {
            res <<=1; //Shift to left
            res |= (n&1); //Add last 
        }
        return res;
    }
};
