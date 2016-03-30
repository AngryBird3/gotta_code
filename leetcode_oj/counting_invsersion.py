#!/usr/bin/python
'''
Count inversion
Given 2 lists, have same element in different orders:
	1	2	3	4	5	6
l1: a	b	d	e	c	f
l2:	b	a	c	f	d	e

Goal:
Count pairs of items that in different orders in two lists

Hint:
Only need one list for index:
For this example, your input should look like:
2	1	5	6	3	4
'''
count = 0
def merge_sort(l):
	#Base case
	if(len(l) < 2):
		return l
	d = len(l)/2
	return merge(merge_sort(l[:d]), merge_sort(l[d:]))

def merge(l, r):
	global count
	i = 0
	j = 0
	result = list()
	while (i < len(l)) and (j < len(r)):
		if(l[i] < r[j]):
			result.append(l[i])
			i+=1
		elif(l[i] > r[j]):
			#invserion
			count += (len(l) - i)
			result.append(r[j])
			j+=1 
	result.extend(l[i:])
	result.extend(r[j:])
	return result

i = [2, 1, 5, 6, 3, 4]
print merge_sort(i)
print "Inversions: ", count
