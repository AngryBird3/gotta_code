/*
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
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class MedianFinder {
	struct min_heap_comp{
  		bool operator()(const int& a,const int& b) const{
    		return a>b;
  		}
	};
	vector<int> min_heap;
	vector<int> max_heap;
	int min_heap_size = 0;
	int max_heap_size = 0;
	double median;
public:
    // Adds a number into the data structure.
    void addNum(int num) {
		/* Algorithm:
		 * - Min heap elements are > current median 
		 * - Max heap elements are < current median
		 * - If # of elements differs by more than 1, remove
		 *   top/root and add into another heap
		 */

		//Add into appropriate heap
		if (!min_heap_size || num > median) {
			min_heap_size++;
			min_heap.push_back(num);
    		// If first time inserting make_heap for min/max heap     
			if (min_heap_size == 1) {
				make_heap(min_heap.begin(), min_heap.end(), min_heap_comp());
			} else {
				push_heap(min_heap.begin(), min_heap.end(), min_heap_comp());
			}
			cout << "Added " << num << " into min heap << (size: " << min_heap_size << ")\n";
		} else {
			max_heap_size++;
			max_heap.push_back(num);
			if (max_heap_size == 1) {
				make_heap(max_heap.begin(), max_heap.end());
			} else {
				push_heap(max_heap.begin(), max_heap.end());
			}
			cout << "Added " << num << " into max heap << (size: " << max_heap_size << ")\n";
		}

		//Balance heaps
		if (min_heap_size - max_heap_size > 1) {
			int n = min_heap.front();
			pop_heap(min_heap.begin(), min_heap.end(), min_heap_comp());
			min_heap.pop_back();
			min_heap_size--;

			max_heap.push_back(n);
			push_heap(max_heap.begin(), max_heap.end());
			max_heap_size++;
		} else if (max_heap_size - min_heap_size > 1) {
			int n = max_heap.front();
			pop_heap(max_heap.begin(), max_heap.end());
			max_heap.pop_back();
			max_heap_size--;

			min_heap.push_back(n);
			push_heap(min_heap.begin(), min_heap.end(), min_heap_comp());
			min_heap_size++;
		}
	
		//Finally set median
		if (min_heap_size == max_heap_size) {
			median = (min_heap.front() + max_heap.front())/double(2);
		} else if(min_heap_size > max_heap_size) {
			median = min_heap.front();
		} else {
			median = max_heap.front();
		}
    }

    // Returns the median of current data stream
    double findMedian() {
    	return median; 
    }
};

int main() {
// Your MedianFinder object will be instantiated and called as such:
   	MedianFinder mf;
	vector<int> n {1,3,7,10,2,0,21};
	for (int i = 0; i < n.size(); i++) {
		mf.addNum(n[i]);
		copy(n.begin(), n.begin()+i+1, ostream_iterator<int>(cout, " "));
		printf("Median: %f\n", mf.findMedian());
	}
	return 0;
}
