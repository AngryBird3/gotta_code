'''
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if not s:
            return s in wordDict

        opt = [0] * (len(s) + 1)

        for i in range(len(s)+1):
            opt[i] = s[:i] in wordDict

        for i in range(0, len(s)+1):
            for j in range(i, len(s)+1):
                opt[j] = opt[j] or opt[i] and s[i:j] in wordDict
                #print "s[i:j]: ", s[i:j], " opt[j]: ", opt[j]
        return opt[-1]
