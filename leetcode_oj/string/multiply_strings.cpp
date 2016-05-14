/*
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
 Facebook Twitter
Hide Tags Math String
Hide Similar Problems (M) Add Two Numbers (E) Plus One (E) Add Binary

Difficulty: Medium
*/
class Solution {
public:
    string multiply(string num1, string num2) {
        /* Algorithm:
            https://www.mathsisfun.com/numbers/multiplication-long.html
            Nothing but how we multiply with pen and paper
            1) Start from backward(10's place)
            2) for ith in num1 and jth in num2 num:
                its result sits in res[i+j+1] += num1[i] * num2[j]
            3) Don't forget carry

            To convert char to int: '0' - '0' ie a - '0'
         */
            
        string res(num1.length() + num2.length(), '0');
            
        int c = 0, s, i, j;
        for (i = num2.length() - 1; i >= 0; i--) {
            for (j = num1.length() - 1; j >= 0; j--) {
                s = res[i +j + 1] - '0' + ((num2[i] - '0') * (num1[j] - '0')) + c;
                res[i + j + 1] = s % 10 + '0';
                c = s / 10; 
            }   
            if (c > 0) {
                res[i] = res[i] + c ; 
            }   
            c = 0;
        }   
        if (res.find_first_not_of('0') != std::string::npos) {
            return res.substr(res.find_first_not_of('0'));
        }
        return "0";
    }
};
