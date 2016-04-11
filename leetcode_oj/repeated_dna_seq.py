#https://leetcode.com/discuss/74330/20-ms-solution-c-with-explanation
#https://leetcode.com/discuss/29419/my-concise-solution-with-c
import hashlib
class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
		result = list()
		# {hash_value_str: true}
		seq_map = {}	
		for i in range(0, len(s) - 9):
			sub_s = s[i:i+10]
			h = hash(sub_s)
			if h in seq_map:
				if sub_s not in result:
					result.append(sub_s)
			else:
				seq_map[h] = True
		return result

sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT" 
print sol.findRepeatedDnaSequences(s)
s = ""
print sol.findRepeatedDnaSequences(s)
s = "AAAAAAAAAAA"
print sol.findRepeatedDnaSequences(s)
s = "AAAAAAAAAAAAAAAAAAAAA"
print sol.findRepeatedDnaSequences(s)
