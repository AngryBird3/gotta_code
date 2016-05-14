'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

Hide Company Tags LinkedIn Uber Facebook
Hide Tags Hash Table Two Pointers String
Hide Similar Problems (H) Substring with Concatenation of All Words (M) Minimum Size Subarray Sum (H) Sliding Window Maximum
Difficulty: Hard
'''
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = {} #hash for char in t
        for l in t:
            try:
                m[l] += 1
            except:
                m[l] = 1
        
        start = 0
        end = 0
        dist = float('inf')
        counter = len(t)
        min_start = 0
        
        while end < len(s):
            if s[end] in m:
                #if char in s exists in t, decrement counter
                if m[s[end]] > 0:
                    counter -= 1
                m[s[end]] -= 1
            
            end += 1
            while counter == 0:
                if end - start < dist:
                    dist = end - start
                    min_start = start
                
                if s[start] in m:    
                    m[s[start]] += 1
                #when char exists in t increment counter
                    if m[s[start]] > 0:
                        counter += 1
                start += 1
        #print dist
        if dist != float('inf'):
            return s[min_start:min_start+dist]
        return ""
