'''
Implement a set-like data structure that supports Insert, Remove, and GetRandomElement efficiently. Example: If you insert the elements 1, 3, 6, 8 and remove 6, the structure should contain [1, 3, 8]. Now, GetRandom should return one of 1, 3 or 8 with equal probability. 
'''
import random
class Set:
    def __init__(self):
        # Key as val
        self.__h = {}
        #Index based access
        self.__index = list()
            
    def insert(self, val):
        if val not in self.__h:
            self.__h[val] = True
            self.__index.append(val)

    def remove(self, val):
        if val in self.__h:
            del self.__h[val]
            self.__index.remove(val)

    def getRandom(self):
        if self.__index:
            return self.__index[random.randint(0, len(self.__index) - 1)]
s = Set()
print s.getRandom() #Que: What to do when set is empty
print s.remove(3) #Que: What to do when set doesn't contain that val
s.insert(1)
s.insert(3)
s.insert(1) #Que: What to do when set already contain that val
s.insert(6)
s.insert(8)
s.remove(6)
print s.getRandom()
print s.__dict__
