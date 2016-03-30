from collections import deque
class Solution:
	# ******** ASSUMING W1 < W2 *********
	def rolling_max_avg(self, a, w1, w2):
		#a: Input array
		#w: window size
		deq_max_w1 = deque([], maxlen=w1)
		deq_max_w2 = deque([], maxlen=w2)
		deq_avg_w1 = deque([], maxlen=w1)
		deq_avg_w2 = deque([], maxlen=w2)
		
		max_w1 = a[0]
		max_w2 = a[0]
		prev_avg = 0
	
		sum_w1 = 0
		for i in range(w1):
			# For avg
			sum_w1 += a[i]
			deq_avg_w1.append(a[i])

			# For max
			while deq_max_w1 and a[i] >= a[deq_max_w1[len(deq_max_w1)-1]]:
				deq_max_w1.pop()
			deq_max_w1.append(i)	
			print "(None, None, None, None)"
	
		sum_w2 = 0
		for i in range(w2):
			# For avg
			sum_w2 += a[i]
			deq_avg_w2.append(a[i])

			# For max
			while deq_max_w2 and a[i] >= a[deq_max_w2[len(deq_max_w2)-1]]:
				deq_max_w2.pop()
			deq_max_w2.append(i)	
		
		for i in range(w1, len(a)):
			'''
				Store output for previous window
			'''
			#for avg
			avg_w1 = sum_w1 / float(w1)
			if i >= w2:
				avg_w2 = sum_w2 / float(w2)
			else:
				avg_w2 = None
			#for max
			max_w1 = a[deq_max_w1.popleft()]
			if i >= w2:
				max_w2 = a[deq_max_w2.popleft()]
			else:
				max_w2 = None

			#print "(", avg_w1, ",", max_w1, ",", avg_w2, ",", max_w2, ")"
			yield (avg_w1, max_w1, avg_w2, max_w2)
			
			# For next window -- MAX
			while (deq_max_w1) and (deq_max_w1[0] <= i - w1):
				deq_max_w1.popleft()

			while deq_max_w1 and a[i] >= a[deq_max_w1[len(deq_max_w1) - 1]]:
				deq_max_w1.pop()

			deq_max_w1.append(i)
			
			# Do same for queue2
			if i >= w2:
				while deq_max_w2 and deq_max_w2[0] <= i - w2:
					deq_max_w2.popleft()

				while deq_max_w2 and a[i] >= a[deq_max_w2[len(deq_max_w2) - 1]]:
					deq_max_w2.pop()

				deq_max_w2.append(i)
	
			#For next window - avg
			sum_w1 = sum_w1 - deq_avg_w1.popleft() + a[i]
			deq_avg_w1.append(a[i])
			if i >= w2:
				sum_w2 -= deq_avg_w2.popleft() + a[i]
				deq_avg_w2.append(a[i])
		
		#for last window
		avg_w1 = sum_w1 / float(w1)
		if i >= w2:
			avg_w2 = sum_w2 / float(w2)
		else:
			avg_w2 = None
		#for max
		max_w1 = a[deq_max_w1.popleft()]
		max_w2 = a[deq_max_w2.popleft()]

		#print "(", avg_w1, ",", max_w1, ",", avg_w2, ",", max_w2, ")"
		yield (avg_w1, max_w1, avg_w2, max_w2)

s = Solution()
a = [i for i in range(23)]
s.rolling_max_avg(a, 3, 20)

