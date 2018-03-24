def solution(E, L):
    # write your code in Python 2.7
	FMT = '%H:%M'
	tdelta = datetime.strptime(E, FMT) - datetime.strptime(L, FMT)
	tdelta = tdelta.seconds/60

	total_hours = 0
	#if its full hour?
		if tdelta % 60 == 0:
		total_hours = tdelta / 60
		else:
		total_hours = tdelta / 60 + 1

		print 'total_hours: ', total_hours 
		ENTRANCE_FEE  = 2
		FIRST_HOUR_COST = 3
		REST_HOUR_COST = 4

		#First hour
		total_cost = 2 + 3
		total_hours -= 1

		if total_hours:
		total_cost += (4 * total_hours)

print solution('09:42', '11:42')
