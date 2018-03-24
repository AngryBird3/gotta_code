'''
Created on Jan 1, 2013

@author: dharadarji

Implement a data structure which does insert(), remove() 
and get_random() in constant time?

Sol:
A map <T, int> M and vector <T> V  would do
a) Insert (X):  push_back X to V and note the index I 
(ie; V.size() - 1). Insert (X, I)  in M.

b) Remove(X): Fetch index I of element X from the map; M[X]; 
swap V[I] and last element 'Y' of V, update M[Y]  to I, erase 
last element of V. Erase key X in M.

c) get_random(): return V[rand(0, V.size()- 1)];
'''
