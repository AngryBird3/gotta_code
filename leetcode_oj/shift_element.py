def shift_elem_clockwise(mat):
	if len(mat) != len(mat[0]):
		return False

	n = len(mat)
	count = 0
	start = 0
	end = n
	end_r = n
	end_c = n

	new_mat = [ [0 for i in range(n)]  for j in range(n)]
	
	while count != n*n:
		#left to right row
		for i in range(start, end_c):
			if i+1 < end_c:
				new_mat[start][i+1] = mat[start][i]	
			else:
				if(start + 1 < end_r):
					#move to next row
					new_mat[start+1][i] = mat[start][i]
				else:
					new_mat[start][i] = mat[start][i]
			count += 1
		if count >= n*n:
			break
		
		#Top to bottom col
		for i in range(start+1, end_r):
			if i+1 < end_c:
				new_mat[i+1][end_c-1] = mat[i][end_c-1]
			else:
				if (end_c - 2 >= start):
					#shift to left
					new_mat[i][end_c-1-1] = mat[i][end_c - 1]
				else:
					new_mat[i][end_c - 1] = mat[i][end_c - 1]
			count += 1


		#Right to left row
		for i in range(end_c - 1 -1, start-1, -1):
			if i - 1 >= start:
				new_mat[end_r - 1][i - 1] = mat[end_r - 1][i]
			else:
				if (end_r - 2 >= start):
					#move to 1 row above
					new_mat[end_r - 1 -1][i] = mat[end_r - 1][i]
				else:
					new_mat[end_r - 1][i] = mat[end_r - 1][i]
			count += 1

		#Bottom to top col
		for i in range(end_r - 1 -1, start, -1):
			if i - 1 >= start:
				new_mat[i - 1][start] = mat[i][start]
			else:
				if (start + 1 <= end_r):
					#Shift to right; doesn't look necessary
					new_mat[i][start + 1] = mat[i][start]
				else:
					new_mat[i][start] = mat[i][start]
			count += 1
		start += 1
		end_c-= 1
		end_r-=1


	return new_mat

def print_mat(mat):
	for i in range(len(mat)):
		print mat[i]
a = [[1, 2, 3, 4],
	 [5, 6, 7, 8],
     [9, 10, 11, 12],
	 [13, 14, 15, 16]]
'''
a = [[1,2,3],
	 [4,5,6],
	 [7,8,9]]
'''
print_mat(shift_elem_clockwise(a))
