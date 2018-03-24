def recurringTask(firstDate, k, daysOfTheWeek, n):
    tasks = []
    date, month, year = map(int, firstDate.split('/'))
    
    t = 1
    tasks.append(firstDate)
    weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
              "Friday", "Saturday"]
    firstDay = weekday.index(daysOfTheWeek[0])
    while t < n:
        for i in range(1, len(daysOfTheWeek)):
            diff = weekday.index(daysOfTheWeek[i]) - firstDay
            nextDay = getNextDay(firstDate, diff+1)
            tasks.append(nextDay)
            t += 1
            if t >= n:
                return tasks
        firstDate = tasks[t - len(daysOfTheWeek)]
        #print "Tasks: ", tasks, " t: ", t
        #print "for next_week calculation, first date: ", firstDate
        nextDay = getNextDay(firstDate, k*7-1)
        #print "Next day for next_week: ", nextDay
        firstDate = nextDay
        tasks.append(nextDay)
        t += 1

    return tasks

def getNextDay(firstDate, days):
    month_len = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date, month, year = map(int, firstDate.split('/'))
    if isLeap(year):
        month_len[1] = 29
    if date + days <= month_len[month - 1]:
        nextDay = str(date + days)
    else:
        print "First date: ", firstDate, " Days: ", days
        #Adjust month/year
        next_date = date
        while days:
            print "next_date: ", next_date, " month: ", month
            if next_date + days > month_len[month - 1]:
                days = days - (month_len[month - 1] - next_date)
                if days:
                    if month == 12:
                        year += 1
                        month = 1
                    else:
                        month += 1
                    next_date = 1
            else:
                next_date += days
                days = 0
        nextDay = str(next_date)
    if len(nextDay) != 2:
        nextDay = "0" + nextDay
    nextDay += "/" + str(month) + "/" + str(year)
    return nextDay
        
def isLeap(year):
    return year % 400 == 0
'''
firstDate = "01/01/2015"
k = 2
daysOfTheWeek = ["Monday", "Thursday"]
n = 4
'''
firstDate = "31/12/2999"
k = 1
daysOfTheWeek = ["Tuesday"]
n = 2
tasks = recurringTask(firstDate, k, daysOfTheWeek, n) 
print "Recurring Tasks: ", tasks
