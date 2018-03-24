'''
How to find the missing k elements out of the unsorted natural N elements
in an integer aray. Range is between 1 and size
The logic is pretty simple - I'm putting every element to corresponding index, e.g. put 3 to index 3, 5 to index 5 e.t.c. If element is greater than the size of array - put -1. And finally just check array for elements equal to "-1".

a = [5,2,2,5,5] 
'''
def missing_two(a, n): 
    for i in range(n):
        k = i 
        print "i: ", i
        while a[k] != k+1:
            #print "a[k]: ", a[k], " k+1: ", k+1, "a[a[k] - 1]: ", a[a[k] - 1]
            if a[k] < 1 or a[k] > n or a[k] == a[a[k] - 1]: 
                a[k] = -1
                print "a: ",a
                break
            a[k], a[a[k] - 1] = a[a[k] - 1], a[k]
            #print "a: ",a
    for i in range(n):
        if a[i] < 0:
            print "missing: ", i+1 
#missing_two([5,1,2,5,5], 5)

def missing_two_1(a, n): 
    for i in range(n):
        print "i: ", i , "a[i]: ", a[i]
        if a[abs(a[i]) - 1] > 0:
            a[a[i] - 1] = -1
        else:
            print "Err: ", a[i]
        print "a: ", a
    for i in range(n):
        if a[i] > 0:
            print i+1 
missing_two_1([5,1,2,5,3],5)

###### Final #######
def missing_two(a, n): 
    for i in range(n):
        k = i 
        print "i: ", i
        while a[k] != k+1:
            print "a[k]: ", a[k], " k+1: ", k+1, "a[a[k] - 1]: ", a[a[k] - 1]
            if a[k] < 1 or a[k] > n or a[k] == a[a[k] - 1]: 
                a[k] = -1
                print "Replacing a[k] with -1: ",a
                break
            temp = a[k]
            a[k] = a[a[k] - 1]
            a[temp - 1] = temp
            #a[k], a[a[k] - 1] = a[a[k] - 1], a[k]
            print "a: ",a
    for i in range(n):
        if a[i] < 0:
            print "missing: ", i+1 
missing_two([5,1,2,5,5], 5)

