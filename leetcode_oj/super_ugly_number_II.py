'''
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000
'''
import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

		'''
		Algorithm:

		This time, I'll push the minimum prime*idx into heap
		so that when I need to increment index, for whoever
		has minimum, it would take o(klogk) where k=|primes|
		'''

		res = [1]
		idx = [0] * len(primes)
		heap = []

		for k, p in enumerate(primes):
			heapq.heappush(heap, (p, k))
			# For first time, as our first ugly
			# number is 1, appending all primes
			# with p and index

		for i in range(1, n):
			min_val, k = heap[0] #First min
			res.append(min_val)

			#Now, whoever got min_val, increment index
			while heap[0][0] == min_val:
				_, k = heapq.heappop(heap)
				idx[k] += 1
				#Add new values into heap
				heapq.heappush(heap, (primes[k] * res[idx[k]], k))

		return res[-1]
