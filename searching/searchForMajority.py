'''
Created on Dec 16, 2012

@author: dharadarji
Stream - long sequence of words - most of them are repeating of W.

Design an algo that reads this stream ONLY ONCE and uses only a
constant amount of memory to find W
'''
'assuming start with majority element'

def searchForMajority(arr):
    count = 0
    'Find majority elem'
    for i in range(len(arr)):
        if count == 0:
            majority_elem = arr[i]
        if arr[i] == majority_elem:
            count+=1
        else:
            count-=1
    print majority_elem
    'check if it occurs at least n/2 times'    
    
arr = ["d","d","d","h","a","h","h","h","a","a","a","d","d","d","d"]
searchForMajority(arr)