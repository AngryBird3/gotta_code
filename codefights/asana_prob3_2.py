def recurringTask(firstDate, k, daysOfTheWeek, n):
    tasks = []
    date, month, year = map(int, firstDate.split('/'))
    
    t = 1
    tasks.append(firstDate)
    weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
              "Friday", "Saturday"]
    firstDay = getDay(firstDate)
    print "FirstDay: ", firstDay
    # When given first date is not starting at first day in given
    # daysOfTheWeek
    if firstDay != weekday.index(daysOfTheWeek[0]):
        print "firstDay is not first"
        covered_days = 1
        while covered_days != len(daysOfTheWeek):
            print "daysOfTheWeek: ", daysOfTheWeek
            print "firstDay: ", firstDay
            index_of_first_day = daysOfTheWeek.index(weekday[firstDay])
            # This check is whether we need to first of days
            # e.g. M W F are daysOfTheWeek and first day
            # is W, then next coming day would be F, 
            # then again we need to go front
            if index_of_first_day < len(daysOfTheWeek) - 1:
                coming_day = index_of_first_day + 1
                diff = weekday.index(daysOfTheWeek[coming_day]) - firstDay
            else:
                coming_day = 0
                diff = 6 - firstDay + weekday.index(daysOfTheWeek[0])
            nextDay = getNextDay(firstDate, diff+1)
            tasks.append(nextDay)
            firstDay = nextDay
            covered_days += 1
            t += 1
            if t >= n:
                return tasks
    else:
        for i in range(1, len(daysOfTheWeek)):
            diff = weekday.index(daysOfTheWeek[i]) - firstDay
            nextDay = getNextDay(firstDate, diff + 1)
            tasks.append(nextDay)
            t += 1
            if t >= n:
                return tasks
        
    firstDate = tasks[0]
    p = 0
    while t < n:
        nextDay = getNextDay(firstDate, k*7)
        tasks.append(nextDay)
        t += 1
        firstDate = tasks[p]
        p += 1
    return tasks

def getNextDay(firstDate, days):
    month_len = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date, month, year = map(int, firstDate.split('/'))
    if isLeap(year):
        month_len[1] = 29
    if date + days <= month_len[month-1]:
        nextDay = str(date + days)
    else:
        #Adjust month/year
        next_date = date
        while days:
            if month > 12:
                assert 0 == "Month is invalid"
            if next_date + days > month_len[month-1]:
                days = days - (month_len[month-1] - next_date)
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
    if len(nextDay) < 2:
        nextDay = "0" + nextDay
    if len(str(month)) < 2:
        month = "0" + str(month)
    nextDay += "/" + str(month) + "/" + str(year)
    return nextDay
        
def isLeap(year):
    return (year % 4 == 0 and year % 100 != 0)

from datetime import date

def getDay(dat):
    day, month, year = dat.split("/")
    #Mon is 1, Sun is 7
    w = date(int(year), int(month), int(day)).isoweekday()
    if w == 7:
        return 0
    return w
''' 
firstDate = "01/01/2015"
k = 2
daysOfTheWeek = ["Monday", "Thursday"]
n = 4
firstDate = "23/02/2000"
k = 2
daysOfTheWeek = ["Wednesday", "Friday"]
n = 4
'''
firstDate = "31/12/2999"
k = 1
daysOfTheWeek = ["Tuesday"]
n = 2
tasks = recurringTask(firstDate, k, daysOfTheWeek, n) 
tasks = recurringTask(firstDate, k, daysOfTheWeek, n) 
print "Recurring Tasks: ", tasks
