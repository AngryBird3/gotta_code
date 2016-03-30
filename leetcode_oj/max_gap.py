#!/usr/bin/python
'''
Given an unsorted array, find the maximum difference between 
the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative 
integers and fit in the 32-bit signed integer range.
'''
import math
class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
		minm = min(num)
		maxm = max(num)

		bucket = {}
		delta = (maxm - minm)/(float(len(num)) - 1)
		print "Delta: ", math.floor(delta)
		bucket_list = list()
		if math.floor(delta) == 0:
			delta += 1
		for i in range(minm, maxm, int(math.floor(delta))):
			bucket[i] = list()
			bucket_list.append(i)
		bucket[maxm] = list()
		bucket_list.append(maxm)
	
		print "Buckets: ", bucket
		for a in num:
			b_p = int(math.floor((a - minm)/delta))
			bucket[bucket_list[b_p]].append(a)

		print "Buckets: ", bucket
		#Step 5
		L = list()
		for k in bucket.keys():
			if bucket[k]:
				t1 = min(bucket[k])
				t2 = max(bucket[k])
				L.append((t1, t2))
		print "L : ", L
		#Step 6
		distance = list()
		for i in range(len(L) - 1):
			distance.append(abs(L[i][1] - L[i+1][0]))
	
		print max(distance)
s = Solution()
#a = [5,2,20,17,3]
#a = [1,7,3,2]
a = [1,1,1,1,1,5,5,5,5,5]
s.maximumGap(a)
