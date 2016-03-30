#!/usr/bin/python
'''
Find the closest pair in given list
'''
from math import sqrt, pow

def distance(a, b):
	return sqrt(pow(a[0] - b[0],2) + pow(a[1] - b[1],2))

def brute_min(points, current=float('inf')):
	if len(points) < 2:
		return current
	else:
		head = points[0]
		del points[0]
		newMin = min([distance(head, x) for x in points])
		newCurrent = min([newMin, current])
		return brute_min(points, newCurrent)

def closest_pair(points):
	n = len(points)
	if n <= 3:
		return brute_min(points)

	#Find median
	mid = n / 2
	mid_point = points[mid]
	
	dl = closest_pair(points[:mid])
	dr = closest_pair(points[mid:])

	d = min(dl, dr)

	#Find near line points
	near_line = filter(lambda x: abs(x[0] - mid_point[0]) < d, points)
	return min([brute_min(near_line), d])

list1 = [(12,30), (40, 50), (5, 1), (12, 10), (3,4)]
print closest_pair(list1)
