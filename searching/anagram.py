'''
Created on Dec 16, 2012

@author: dharadarji

Given a dictionary of English words, return the set of all words
grouped into subset of words that are all anagrams  of each other.
'''
def sort_string(word):
    list_word = list(word)
    list_word.sort()
    return str(list_word)

def anagrams(dictionary):
    my_dict = {}
    
    for word in dictionary:
        'sort the word'
        sorted_word = sort_string(word)
        if sorted_word not in my_dict:
            my_dict[sorted_word] = [word]
        else:
            my_dict[sorted_word].append(word)
            
    'print anagram'
    output = []
    for k in my_dict.keys():
        if len(my_dict[k]) > 1:
            output.append(my_dict[k])
    
    print output
    
anagrams(("algorithm", "god", "logarithm", "dog", "app", "paa", "am", "ah", "ma", "ha", "reserve", "reverse"))