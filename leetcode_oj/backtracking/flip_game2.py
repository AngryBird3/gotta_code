'''
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.
'''
class Solution(object):
	def canWin(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		'''
		Algorithm:
		Try ALL possible cases, first and second person can take turn
		If second person is always loosing, first person wins
		'''

		for i in range(len(s)):
			if s[i:i+2] == "++":
				#See if second person looses, with this move, then first wins
				if not self.canWin(s[:i] + "--" + s[i+2:]):
					return True
		#No way this s can win
		return False

	def canWin_dp(self, s, res = {}):
		"""
		:type s: str
		:rtype: bool
		"""
		'''
		Algorithm:
		Try ALL possible cases, first and second person can take turn
		If second person is always loosing, first person wins

		Store each state res
		'''
		if s in res:
			return  res[s]

		for i in range(len(s)):
			if s[i:i+2] == "++":
				#See if second person looses, with this move, then first wins
				if not self.canWin(s[:i] + "--" + s[i+2:]):
					res[s] = True
					res[s[:i] + "--" + s[i+2:]] = False
					return True
		#No way this s can win
		res[s] = False
		return False

s = Solution()
print s.canWin_dp("++++")
