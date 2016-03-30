'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.
'''
class Solution(object):
	def nthUglyNumber(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n <= 5:
			return n
		l1 = list()
		l2 = list()
		l3 = list()
			
		l1 = [3, 4, 5] # l1 * 2
		l2 = [3, 4, 5] # l2 * 3
		l3 = [2, 3, 4, 5] # l3 * 5

		for i in range(6, n+1):
			if l1[0]*2 <= l2[0]*3 and l1[0]*2 <= l3[0]*5:
				num = l1[0]*2
				l1.pop(0)
				if l2[0]*3 == num:
					l2.pop(0)
				if l3[0]*5 == num:
					l3.pop(0)
			elif l2[0]*3 <= l1[0]*2 and l2[0]*3 <= l3[0]*5:
				num = l2[0]*3
				l2.pop(0)
				if l3[0]*5 == num:
					l3.pop(0)
			#if l3[0]*5 <= l1[0]*2 and l3[0]*5 <= l2[0]*3:
			else:
				num = l3[0]*5
				l3.pop(0)
			l1.append(num); l2.append(num); l3.append(num)
			#print "i: ", i, "num: ", num
			#print l1
			#print l2
			#print l3
		return num

	def nthUglynum2(self, n):
		ugly = [1]
		i2, i3, i5 = 0, 0, 0
		for i in range(n-1):
			u2, u3, u5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
			umin = min((u2, u3, u5))
			if umin == u2:
				i2 += 1
			if umin == u3:
				i3 += 1
			if umin == u5:
				i5 += 1
			ugly.append(umin)
		return ugly[-1]
s = Solution()
#print s.nthUglyNumber(6)
print s.nthUglynum2(10)

