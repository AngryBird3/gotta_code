'''
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

Hide Tags Dynamic Programming String
Difficulty: Hard

Consider: s= AAB, and T = AB
'''
class Solution(object):
    def numDistinct(self, s, t):
        """
            :type s: str
             :type t: str
             :rtype: int
             """
             if not s or not t:
             return 0
#opt[i][j] = # of subseq s[..i] and t[..j]
             opt = [[0 for j in range(len(t))] for i in range(len(s))]

             opt[0][0] = 1 if s[0] == t[0] else 0
             for i in range(1, len(s)):
                 if s[i] == t[0]: 
                 opt[i][0] = opt[i-1][0] + 1
                 else:
                 opt[i][0] = opt[i-1][0]

#for j in range(1, len(t)):
#   opt[0][j] = opt[0][j-1]

#for i in range(len(opt)):
#   print ""
#   for j in range(len(opt[i])):
#       print opt[i][j], 

                 for i in range(1, len(s)):
                     for j in range(1, len(t)):
                         if s[i] == t[j]:
                         opt[i][j] = opt[i-1][j] + opt[i-1][j-1]
                         else:
                         opt[i][j] = opt[i-1][j]

                         return opt[-1][-1]
