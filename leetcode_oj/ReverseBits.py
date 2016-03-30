'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 
(represented in binary as 00000010100101000001111010011100), 
return 964176192 (represented in binary as 00111001011110000010100101000000).
'''
import numpy as np
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
		ii32 = np.iinfo(np.int32)
		if n >= ii32.max or n <= ii32.min:
			return 0
		binary_of_n = self.to_binary(n)
		binary_of_n.reverse()
		#print "To binary: ", ''.join(str(a) for a in binary_of_n)
       	dec_of_n = self.from_binary(binary_of_n) 
		return dec_of_n

    def to_binary(self, n):
		binary = list()
		while(n):
			mod = n % 2;
			binary.append(mod)
			n = n / 2;
		binary.reverse()
		l = len(binary)
		x = 32 - l
		if x < 0:
			return [0]
		binary = [0]*x + binary
		return binary

    def from_binary(self, binary):
		decimal = 0
		for i in range(len(binary)-1, -1, -1):
			decimal += pow(2,len(binary)-i-1) * binary[i]
			#print "binary[",i,"]: ", binary[i], " Decimal: ", decimal
		return decimal

s = Solution()
n = 2900971227
print "Reverse bits of: ", n
print s.reverseBits(n)
