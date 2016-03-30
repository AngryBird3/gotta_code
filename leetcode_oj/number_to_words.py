'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
'''
class Solution(object):
	def __init__(self):
		self.str_num = {	0: "",
				   	1: "One",
				   	2: "Two",
				   	3: "Three",
					4: "Four",
					5: "Five",
					6: "Six",
					7: "Seven",
					8: "Eight",
					9: "Nine",
					10: "Ten",
					11: "Eleven",
					12: "Twelve",
					13: "Thirteen",
					14: "Fourteen",
					15: "Fifteen",
					16: "Sixteen",
					17: "Seventeen",
					18: "Eighteen",
					19: "Nineteen",
					20: "Twenty",
					30: "Thirty",
					40: "Forty",
					50: "Fifty",
					60: "Sixty",
					70: "Seventy",
					80: "Eighty",
					90: "Ninty" }

	''' Convert two digit num to word '''		
	def two(self, num):
		if len(num) == 1:
			return self.str_num[num[0]]
		if num[0] == 0:
			return self.str_num[num[1]]
		if num[0] == 1:
			return self.str_num[num[0]*10+num[1]]
		if num[0] == 2:
			return self.str_num[20] + " " + self.str_num[num[1]]
		if num[0] == 3:
			return self.str_num[30] + " " + self.str_num[num[1]]
		if num[0] == 4:
			return self.str_num[40] + " " + self.str_num[num[1]]
		if num[0] == 5:
			return self.str_num[50] + " " + self.str_num[num[1]]
		if num[0] == 6:
			return self.str_num[60] + " " + self.str_num[num[1]]
		if num[0] == 7:
			return self.str_num[70] + " " + self.str_num[num[1]]
		if num[0] == 8:
			return self.str_num[80] + " " + self.str_num[num[1]]
		if num[0] == 9:
			return self.str_num[90] + " " + self.str_num[num[1]]
	
	def three(self, num):
		if num[0] == 0:
			return self.two(num[1:])
		#return based on size
		if len(num) == 1:
			return self.str_num[num[0]] 
		if len(num) == 2:
			return self.two(num)
		return self.str_num[num[0]] + " Hundred " + self.two(num[1:])

	def numberToWords(self, num):
		"""
		:type num: int
		:rtype: str
		"""

		if num == 0:
			return "zero"

		#Convert num into nums (list)
		nums = list()
		n = num
		while num:
			nums.insert(0, num % 10)
			num = num / 10
		if n < 100:
			return self.two(nums)
		if n < 1000:
			return self.three(nums)

		# place one: Thousand, two: million, three: billion
		place = 0 
	
		res = ""
		#Convert for place 0 (first three digit)
		res = self.three(nums[-3:])
		place += 1
		i = 6
		#for i in range(6, len(nums)):
		while True:
			if not nums[-i:-i+3]:
				break
			#print "Next chunk: ", nums[-i:-i+3]
			t = self.three(nums[-i:-i+3])
			if place == 1 and t:
				res = t + " Thousand " + res 
			elif place == 2 and t:
				res = t + " Million " + res
			elif place == 3 and t:
				res = t + " Billion " + res
			place += 1
			i += 3
		return res

s = Solution()
print s.numberToWords(20)
