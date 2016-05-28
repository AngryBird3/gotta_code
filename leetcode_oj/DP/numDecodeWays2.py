class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        opt = [0] * (len(s)+1)
        opt[0] = 1
        #opt[i] = opt[i-1] #if s[i-1] != 0
        #           + opt[i-2] #if s[i-1] > "09" and s[i-1] < "27"
        #i-1th digit 
        for i in range(1, len(s)+1):
            if s[i-1] != "0":
                opt[i] += opt[i-1]
            if i != 1 and s[i-2:i] > "09" and s[i-2:i] < "27":
                opt[i] += opt[i-2]
        return opt[len(s)]
