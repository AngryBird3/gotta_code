'''
Created on Dec 25, 2012

@author: dharadarji

Given: Two same length string (words that exists in dictionary)
Goal: Given two word of equal length that are in dictionary , 
      write a method to transform one word into another word by 
      changing only one letter at a time. The new word you get in 
      each step must be in the dictionary.
Example:
I: DAMP,LIKE
O: DAMP-> LAMP-> LIMP -> LIME -> LIKE.

My Solution isn't checking, new word we get in each step exists in
dictionary
Reference: http://bioinfo.ict.ac.cn/~dbu/AlgorithmCourses/Lectures/Lec6-EditDistance.pdf
'''

'''
EditDistance(s1, s2): convert word2 to word1, changing one letter 
at a time
e.g. word2 = SPAKE, word1 = PARK
'''
def EditDistance(word1, word2):
    word1.capitalize()
    word2.capitalize()
    len1 = len(word1) #vertically
    len2 = len(word2) #horizontally
    #Allocate the table
    table = [None]*(len2+1) #Num of rows (SPARK)
    for i in range(len2+1): 
        table[i] = [0]*(len1+1) #Num of columns (PARK)
    
    # Initialize the table
    for i in range(1, len2+1): 
        table[i][0] = i
    for i in range(1, len1+1): 
        table[0][i] = i
    #This is not needed as I'm printing "change" at each step <<< Not possible
    
    #DP
    for i in range(1, len2+1):
        for j in range(1, len1+1):
            #print "*** DEBUG ***", word1[j], word2[i]
            if word1[j-1] == word2[i-1]:
                d = 0
            else:
                d = 1
            'Do DP'
            table[i][j] = min(table[i-1][j-1] + d,
                              table[i-1][j] + 1,
                              table[i][j-1] + 1)
    print "Final cost - ", table[len2-1][len1-1]
    for i in range(0, len2+1):
        print table[i][0:len1]

word1 = "park"
word2 = "spake"
EditDistance(word1, word2)
        