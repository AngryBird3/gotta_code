'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''
class Solution(object):
	def simplifyPath(self, path):
		"""
		:type path: str
		:rtype: str
		"""
		if not path:
			return "/"

		stack = list()
		path = path.split("/")
		res = ""
		for d in path:
			if not d:
				continue
			elif d == ".":
				#Still current dir path
				#no need to append on stack
				continue
			elif d == "..":
				#pop
				if stack:
					stack.pop()
			else:	
				stack.append(d)

		res ="/"+ "/".join(stack)
		return res

s = Solution()
print s.simplifyPath("/../")
