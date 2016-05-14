/*
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
*/
class Solution {
public:
    int myAtoi(string str) {
        if (str.empty())
            return 0;
            
        int result = 0, i = 0;
        bool negative_sign = false;
        while(isspace(str[i])) {
            i++;
        }
        if (str[i] == '-') {
            negative_sign = true;
            i++;
        } else if (str[i] == '+') {
            i++;
        }
        
        for(; i < str.length(); i++) {
            //ascii values of the digits 1-9 are off by 48 (0 is 48, 9 is 57)
            int t = int(str[i]);
            if (t < 48 || t > 57) {
                break;
            }
            if((result < INT_MAX/10) || (result == INT_MAX/10 && (t - 48 <= 7))) {
                result = result * 10 + (t - 48);
            } 
            else {
                if (negative_sign) {
                    return INT_MIN;
                } else {
                    return INT_MAX;
                }
            }
        }

        if (negative_sign) {
            return -result;
        } else {
            return result;
        }
    }
};
