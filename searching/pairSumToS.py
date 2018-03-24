'''
Created on Dec 16, 2012

@author: dharadarji

Search for a pair which sums to S from an array

O(n)
'''

def pairSum(arr, K):
    h = {}
    for i in range(len(arr)):
        complement = K - arr[i]
        'store num and its index'
        h[arr[i]] = i
        if complement in h:
            'which 2 indexes sum to K'
            if i != h[complement]:
                print "For sum: ", K, " Indexes: ", h[complement], i 
    
        
arr = [2, 3, 4, 5, 6, 7, 8, 7]

pairSum(arr, 4)
pairSum(arr, 5)
pairSum(arr, 13)
pairSum(arr, 15)
pairSum(arr, 17)