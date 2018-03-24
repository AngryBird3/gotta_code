'''
Created on Jan 13, 2013

@author: dharadarji

To find all permutation starting at position i,
successively place "all allowable letters" in position i, 
and for each new letter in position i, find all 
permutations starting at position i+1 (the recursive case)

when i is greater than then length of input string, A 
permutation has been completed; print it and return to changing
letters at position less than i (the base case)

"All allowable letters" - which aren't used  
'''

def permute(inString):
    length = len(inString)
    out = [None]*length
    used = [0]*length
        
    doPermute(inString, out, used, length, 0)
    return 1

def doPermute(inString, out, used, length, recursLev):
    'Base case'
    if recursLev == length:
        print out
        return
    #print "***"
    'Recursive case'
    for i in range(length):
        if used[i]:
            continue
        print "i = ", i, "out = ", out, "recursLev = ", recursLev
        out[recursLev] = inString[i] #Put current letter in output
        used[i] = 1 #mark this letter as used
        doPermute(inString, out, used, length, recursLev+1)
        #print "unmark i = ", i
        used[i] = 0 #unmark this letter
        
        
permute("abc")
        