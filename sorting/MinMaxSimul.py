'''
Created on Dec 16, 2012

@author: dharadarji
'''

'Input'
a = [27,15,10,30,12,17,5,25]

size = len(a)

#Odd elements
if size % 2 != 0:
    minm = a[0]
    maxm = a[0]
    index = 1
else:
    #even elements
    # comparison
    if(a[0] < a[1]):
        minm = a[0]
        maxm = a[1]
    else:
        minm = a[1]
        maxm = a[0]
    index = 2
    
# loop n/2 times
for i in range(index, size, 2):
    # comparison
    if a[i] < a[i+1]:
        small = a[i]
        big = a[i+1]
    else:
        small = a[i+1]
        big = a[i]
    # comparison
    if small < min:
        minm = small
    # comparison
    if big > max:
        maxm = big

print "Min: " , minm , " Max: " , maxm

