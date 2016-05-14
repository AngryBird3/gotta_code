class Solution(object):
    def isOneEditDistance(self, s1, s2):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s1 and not s2:
            return False
        if abs(len(s1) - len(s2)) > 1:
            return False

        if len(s2) > len(s1):
            return self.isOneEditDistance(s2, s1) 

        count = 0 
        len_same = 1 if abs(len(s1) - len(s2)) == 0 else 0 
        j = 0 
        for i in range(len(s1)):
            if j >= len(s2):
                if (len(s1) - i) > 1:
                    #If more than one char remaining its False
                    return False
                else:
                    #only 1 char remainig then, our count should be 0
                    return count == 0
            if s1[i] == s2[j]:
                j += 1
                continue
            count += 1
            if count > 1:
                return False
            if len_same:
                j += 1
            #if len_same that means this is our first "insertion" (or could be delete)
        return count <= 1
