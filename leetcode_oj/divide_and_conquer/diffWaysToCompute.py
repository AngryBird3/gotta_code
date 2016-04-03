'''
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
'''
class Solution(object):
	def diffWaysToCompute(self, s):
		"""
		:type input: str
		:rtype: List[int]
		"""
		'''
		Algorithm:
		1) how do you actually do in paper?
		* n1 op n2 op n3
		* left_num_computation op right_num_Computation 
		* n1 op (n2 op n3) AND (n1 op n2) op n3
		* At each operand do recursively left_side computation ,
		* right side computation
		'''
		res = list()
		#Terminate condition
		#if s is lonely number left
		if s.isdigit():
			return [int(s)]
		for i in range(len(s)):
			#If s[i] is operand
			if s[i] in "-*+":
				res_l = self.diffWaysToCompute(s[:i])
				res_r = self.diffWaysToCompute(s[i+1:])
				for l in res_l:
					for r in res_r:
						res.append(self.compute(l, r, s[i]))
		return res
		
	def compute(self, n1, n2, op):
		if op == "+":
			return n1 + n2
		elif op == "*":
			return n1 * n2
		else:
			return n1 - n2

sol = Solution()
print sol.diffWaysToCompute("2*3-4*5")
