class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        #compute longest prefix-suffix
        lps = self.helper(needle)

        i = 0#Index of haystack
        j = 0#Index of pattern

        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                #See we already found needle
                if j == len(needle):
                    return i-j #start
            else:
                #Move j to next after already matched char
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1

    def helper(self, needle):
		'''
		 lps[i] = the longest proper prefix of pat[0..i] 
              which is also a suffix of pat[0..i]. 

		pat = abcabx 
		so when we have mismatch at x, we look should we go back
		to pat[0] or is there prefix which is also suffix just before
		x. Yes, ab, so we'll start at c.


		https://www.youtube.com/watch?v=GTJr8OvyEVQ
		'''
        i = 1 
        j = 0 
        lps = [0] * len(needle)
        while i < len(needle):
            if needle[i] != needle[j]:
                if j != 0:
                    j = lps[j-1]
                    # Don't incrememnt i here, we need to see if modified j
                    # is same as current i
                else:
                    lps[i] = 0 
                    i += 1
            else:
                lps[i] = j + 1 
                j += 1
                i += 1
        return lps
