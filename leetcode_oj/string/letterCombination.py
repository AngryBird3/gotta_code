'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Difficulty: Medium
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = { '2' : 'abc',
              '3' : 'def',
              '4' : 'ghi',
              '5' : 'jkl',
              '6' : 'mno',
              '7' : 'pqrs',
              '8' : 'tuv',
              '9' : 'wxyz' }
            
        res = list()
        for i in range(len(digits)):
            res = self.combine(d[digits[i]], res)
        return res 

    def combine(self, s1, res):
        if not res:
            res.extend(list(s1))
            return res 
        n_r = list()
        for i in range(len(res)):
            for j in range(len(s1)):
                n_r.append(res[i] + s1[j])
        return n_r 
