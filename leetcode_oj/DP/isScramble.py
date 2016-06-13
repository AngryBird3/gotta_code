'''
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Hide Tags Dynamic Programming String
Difficulty: Hard
'''
class Solution(object):
    def __init__(self):
        self.opt = {}
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # OF course length should be same
        if len(s1) != len(s2):
            return False

        # Ok, both the string character should match, any extra char
        # means its not scramble!
        if sorted(s1) != sorted(s2):
            return False
       
        # If we already found result stored ..  
        if (s1, s2) in self.opt:
            return self.opt[(s1, s2)]   

        # base case s1 == s2 or s1 == rev(s2)
        if len(s1) == 2:
            if s1 == s2: 
                return True
            if s1[0] == s2[1] and s1[1] == s2[0]:
                return True
            else:
                return False

        if len(s1) == 1:
            return s1 == s2
                

        # s1 to be scramble string of s2
        # Divide into two parts any where
        # lets say s11, s12 and s21, s22
        # if scrambled(s11, s21) && s(s12, s22)
        # of scramnled(s11, s22) && s(12, s21)
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) \
                or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                self.opt[(s1,s2)] = True
                return True

        self.opt[(s1, s2)] = False
        return False
