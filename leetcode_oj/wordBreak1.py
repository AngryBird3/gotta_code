'''
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        opt = [False] * (len(s)+1) # s[..i] word break?
        opt[0] = True
        for i in range(len(s)):
            if not opt[i]: #should continue from match position, as in if the word matched at 4, we can start from 2/3
                continue
            for w in wordDict:
                end = i + len(w)
                if end > len(s) or opt[end]:
                    continue
                print "w: ", w, " substr: ", s[i:end], " w==substr: ", w == s[i:end]
                if s[i:end] == w:
                    opt[end] = True
                    
        return opt[len(s)]
