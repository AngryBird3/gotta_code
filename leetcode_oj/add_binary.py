def add_binary(str1, str2):
	str1_len = len(str1) #1100011
	str2_len = len(str2) #     10

	c = 0
	result = ""
	if str1_len > str2_len:
		j = str1_len - 1
		small_str_len = str2_len
		big_str_len = str1_len
		big_str = str1
		small_str = str2
	else:
		j = str2_len - 1
		small_str_len = str1_len
		big_str_len = str2_len
		big_str = str2
		small_str = str1
	for i in range(small_str_len - 1, -1, -1):
		r = int(small_str[i]) + int(big_str[j]) + c
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
		print result

	for i in range(big_str_len - small_str_len - 1, -1, -1):
		r = c + int(big_str[i])
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
	return result
s1 = "1100011"
s2 = "10"
print add_binary(s2, s1) 
