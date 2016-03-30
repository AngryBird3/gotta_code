'''
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''
class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
	def minDistance(self, word1, word2):
		if not word1 and not word2:
			return 0
		if not word1 and word2:
			return len(word2)
		if word1 and not word2:
			return len(word1)

		#Row: word2, col: word1
		d = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
		for i in range(1, len(d)):
			d[i][0] = i
		for j in range(1, len(d[0])):
			d[0][j] = j
		print "len(d): ", len(d)
		for i in range(1, len(d)):
			for j in range(1, len(d[0])):
				#print "i: ", i, " j: ", j, "word1[i-1]: ", word1[i-1], " word[j-1]: ", word2[j-1]
				#self.print_matrix(d)
				# IF X_i == Y_j
				#no_cost = delete_cost = replace_cost = float('inf')
				if word1[i-1] == word2[j-1]:
						d[i][j] = d[i-1][j-1]
				else:
					#delete_cost = d[i-1][j] + 1
					#insert_cost = d[i][j-1] + 1	
					#replace_cost = d[i-1][j-1] + 1
					d[i][j] = min(d[i-1][j-1], d[i-1][j], d[i][j-1]) + 1


		return d[i][j]
	def print_matrix(self, d):
		for i in range(len(d)):
			print ""
			for j in range(len(d[i])):
				print d[i][j], 
		print ""

s = Solution()
print s.minDistance("dhara","dhadra")
