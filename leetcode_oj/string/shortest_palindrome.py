'''
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".

Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases. Thanks to @Freezen for additional test cases.

Hide Company Tags Pocket Gems Google
Hide Tags String
Hide Similar Problems (M) Longest Palindromic Substring (E) Implement strStr() (H) Palindrome Pairs

'''

'''
Notes:
Manacher's Algorithm for finding longest palindrome in string:


https://www.youtube.com/watch?v=nbTSfrEfo6M
Till 11:43.


For this problem: 
I need to find longest palindrome  STARTING at index 0..i.
then append [i..n] in reverse order at beginning.


I'm using Kanacher's algorithm to find Longest palindrome substring, which
STARTS at index 0

In other words, palindrome center whose radius (left) touches 0.

For Mancher's algorithm update rule:

if len(mirror) goes beyond L:
    P[i] = (R-i)
else if its within L:
    P[i] = P[mirror]
expand beyond the minimum length from 1 and 2

In Manacher’s algorithm, s is converted to a string newS splitted by #, for example abc -> #a#b#c#. And we know that p[i] is the len of palindrome whose center is newS[i], and i - P[i] is the actually LEFT of palindrome in s. So we only need to find the last i whose LEFT reaches the start of newS.
'''
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        t = ['#'] * (2* n + 3)
        t[0] = '$'
        t[-1] = '@'
        for i in range(n):
            t[2*(i+1)] = s[i]
            
        n = len(t)
        p = [0] * n
        
        C = 0; R = 0
        
        for i in range(1,n-1):
            mirr = 2*C - i
            
            #if i is within range of previous pal
            if i < R:
                p[i] = min(R-i, p[mirr])
                
            #Expand beyond known one (p[i])
            while  t[i - (1+p[i])] == t[i + (1+p[i])]:
                p[i] += 1
                
            #Update center
            if (i + p[i]) > R:
                c = i
                R = i + p[i]
        
        #Next step is to find Longest palindrome whose left touches 1
        for i in range(n-2, -1, -1):
            if i - p[i] == 1:
                #So left touches start - 0th index
                #The TOTAL len is p[i], hence in orginal FROM p[i]
                #is the guy we wanted for reverse
                return s[p[i]:][::-1] + s
        return s
