'''
Created on Jan 13, 2013

@author: dharadarji

Algorithm:
For each letter in inString from start to end:
    select the current letter in output string
    print the letter in output string
    if the current letter isn't the last letter in input string:
        generate the remaining combinations starting at next
        position with iteration starting at next letter beyond
        the letter you just selected
'''

def combine(inString):
    length = len(inString)
    out = [None]*length
    doCombine(inString, out, length, 0, 0)
    
def doCombine(inString, out, length, recursLev, start):
    for i in range(start, length):
        out[recursLev] = inString[i]
        if recursLev < length - 1:
            out[recursLev + 1] = None
        print out
        
        if i < length - 1:
            doCombine(inString, out, length, recursLev + 1, i + 1)

combine("wxyz")