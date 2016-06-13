class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.paths = []
        self.helper(0, num, target, 0, "", 0)
        return self.paths
        
    def helper(self, start, num, target, cur, path, last):
        #print "path: ", path, " cur: ", cur, " last: ", last
        if start == len(num) and cur == target:
            self.paths.append(path)
            return
            
        for i in range(start, len(num)):
            val = num[start:i+1]
            #We don't also want: 05, anything STARTING with 0, break!
            if num[start] == '0' and i > start:
                break
            if start == 0:
                self.helper(i+1, num, target, cur + int(val), path + val, int(val)) #No sign, for first time
            else:
                self.helper(i+1, num, target, cur + int(val), path + "+" + val, int(val))
                self.helper(i+1, num, target, cur - int(val), path + "-" + val, -int(val))
                '''
                Why not this?
                self.helper(i+1, num, target, cur * int(val), path + "*" + val)
                consider 1 + 2 * 3:
                cur= 3, val=3, res = 9. Instead it should be: 1 + 2 -2 + 2*3
                i.e. cur - last + last*val
                
                When to update last?
                - for op +/- : last = val or -val
                - for op * : last = 
                lets see :
                3 * 3 * 2
                cur= 9
                last=?
                val = 2
                9 + ? - ?*2 = 18
                > how about 1?
                9 * 1 - 1 * 2= 9 - 2===> Incorrect
                
                > last = val*last for multiplication, as that is the value TO BE MULTIPLIED next time
                like for + it was +val, we multiply with last*current val
                '''
                self.helper(i+1, num, target, cur - last + last * int(val), path + "*" + val, int(val) * last)
                
                
