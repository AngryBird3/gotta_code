def add_binary(s1, s2):
	if len(s1) > len(s2):
		s2 = "".join(["0"] * (len(s1) - len(s2))) + s2
	else:
		d = len(s2) - len(s1)
		s1 = "".join(["0"] * d) + s1

	print s1
	print s2
	c = 0
	result = ""
	for i in range(len(s1) - 1 , -1, -1):
		r = int(s1[i]) + int(s2[i]) + c
		if r == 0:
			result = "0" + result
			c = 0
		elif r == 1:
			result = "1" + result
			c = 0
		elif r == 2:
			result = "0" + result
			c = 1
		else:
			result = "1" + result
			c = 1

	if not c:
		c = ""
	return str(c) + result

s1 = "10"
s2 = "1100011"
print add_binary(s2, s1)
