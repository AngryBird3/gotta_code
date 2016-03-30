def is_two_pw(n):
	binary = to_binary(abs(n))
	c = 0
	for b in binary:
		if b == 1:
			c += 1
			if c > 1:
				return False
	return True
	
def to_binary(n):
	binary = list()
	while n:
		binary.append(n%2)
		n = n/2
	return binary	

print is_two_pw(2048)
