'''
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
'''
import collections
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
	def findLadders(self, start, end, dict1):
		#Add end word in dict
		dict1.add(end)
		level_tracker = collections.defaultdict(set)
		parents_tracker = {}
		last = set([start])
		
		while last and end not in level_tracker:
			current = set([])
			level_tracker.clear()
			#print "_______________"
			#print "last: ", last
			#print "parents_tracker: ", parents_tracker

			for word in last:
				for next_word in self.generate_new_word(word, dict1):
					if next_word not in parents_tracker:
						current.add(next_word)
						level_tracker[next_word].add(word)
			#print "level_tracker: ", level_tracker
			#print "current: ", current
			parents_tracker.update(level_tracker)
			last = current
		return [] if not last else self.generate_paths(start, end, parents_tracker)

	
	def generate_new_word(self, word, wordDict):
		alphabets = set("abcdefghijklmnopqrstuvwxyz")
		for i in range(len(word)):  
			for c in alphabets:
				# Replace ith word with alaphabets
				next_word = word[:i] + c + word[i+1:]
				if next_word in wordDict:
					yield next_word

	def generate_paths(self, start, end, parents_tracker):
		#print "Generate paths from parents_tracker"
		#print "parents_tracker: ", parents_tracker
		ret = [[end]]
		while ret[-1][0] != start:
			new_ret = []
			for path in ret:
				#We are interested in just appended/recent node's parent hence path[0]
				for parent in parents_tracker[path[0]]:
					new_ret.append([parent] + path)
			ret = new_ret
		return ret
s = Solution()
print s.findLadders("hit", "cog", set(["hot","dot","dog","lot","log"]))

