'''
iven numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Apple Twitter
Hide Tags Array
Hide Similar Problems (E) Pascal's Triangle II

Difficulty: Easy
'''
class Solution(object):
    def generate(self, numRows):
		"""
		:type numRows: int
		:rtype: List[List[int]]
		"""
		res = list()
		res.append([1])	
		for i in range(1, numRows):
			temp = list()
			temp.append(1)
			for j in range(1, i):
				temp.append(res[i-1][j-1] + res[i-1][j])	
			temp.append(1)			
			res.append(temp)

		return res

s = Solution()
res = s.generate(5)
for i in range(len(res)):
	for j in range(len(res[i])):
		print res[i][j], " ", 
	print ""
