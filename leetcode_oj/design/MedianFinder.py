'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3) 
findMedian() -> 2
Credits:
Special thanks to @Louis1992 for adding this problem and creating all test cases.

Hide Company Tags Google
Hide Tags Heap Design
Difficulty: Hard
'''
from heapq import heappush, heappop
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._max_heap = []
        self._min_heap = []
        self._max_heap_size = 0
        self._min_heap_size = 0
        self.median = None
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        '''
        Algorihtm:
        - Min heap elements > current median
        - Max heap elements < current median
        - if # of elements differs by more than 1, remove
          top/root and add into another heap
        '''
        #Adding num into appropriate heap
        if not self._min_heap_size or num > self.median:
            heappush(self._min_heap, num)
            self._min_heap_size += 1
        else:
            heappush(self._max_heap,  - num) #Max heap: inserting -ve
            self._max_heap_size += 1

        #Balance heaps
        if self._min_heap_size - self._max_heap_size > 1:
            n = heappop(self._min_heap)
            self._min_heap_size -= 1
            heappush(self._max_heap, 0 - n)
            self._max_heap_size += 1
        elif self._max_heap_size - self._min_heap_size > 1:
            n = heappop(self._max_heap)
            self._max_heap_size -= 1
            heappush(self._min_heap, 0 - n) #Adding positive #
            self._min_heap_size += 1

        #Setting median
        if self._min_heap_size == self._max_heap_size:
            self.median = (self._min_heap[0] + (0-self._max_heap[0]))/2.0
        elif self._min_heap_size > self._max_heap_size:
            self.median = self._min_heap[0]
        else:
            self.median = 0 - self._max_heap[0]
            

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        return self.median        

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(-1),mf.findMedian(),mf.addNum(-2),mf.findMedian(),mf.addNum(-3),mf.findMedian(),mf.addNum(-4),mf.findMedian(),mf.addNum(-5),mf.findMedian()
print mf.findMedian()
