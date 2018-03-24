'''
Created on Feb 21, 2013

@author: dharadarji
'''

def get_row(row_index):
    entry = [1]
    
    if row_index == 0:
        return entry
    
    tmp = []
    
    for i in range(1, row_index + 2):
        tmp = entry
        print "i: ", i, "tmp: ", tmp

        entry = []
        entry.append(1)
        
        for j in range(1, i-1):
            print "j: ", j, "tmp[j]: ", tmp[0]
            entry.append(tmp[j-1] + tmp[j])
            
        entry.append(1)
        print "entry: ", entry
    print entry
    
get_row(3)