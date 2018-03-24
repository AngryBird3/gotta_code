'''
Created on Jan 13, 2013

@author: dharadarji
1 digit changed
input: 3
output:
000
001
010
011
100
101
110
111
'''
ans = []
def binary(s, num):
    if num == 0:
        ans.append(s)
    else:
        binary(s+"0", num - 1)
        binary(s+"1", num - 1)
        
binary("", 3)
print ans
    