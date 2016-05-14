'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

Hide Company Tags Microsoft Bloomberg Facebook
Hide Tags Array Two Pointers
Hide Similar Problems (E) Merge Two Sorted Lists
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        '''
        Algorithm:
            Start from back of the array
            if n1 > n2:
                copy n1 to end
                n1_index--
            elif n2 > m1:
                copy n2 to end
                n2_index--
            else:
                copy n1,n2 to end
                n1_index--
                n2_index--
                end--
            end--
        '''
        end = m + n - 1 #0 based index
        n1 = m-1 
        n2 = n-1 
        while n1 >= 0 and n2 >= 0:
            #print "... nums1: ", nums1[n1], " ..nums2: ", nums2[n2]
            if nums1[n1] >= nums2[n2]:
                nums1[end] = nums1[n1]
                n1 -= 1
            elif nums2[n2] > nums1[n1]:
                nums1[end] = nums2[n2]
                n2 -= 1
            end -= 1
            #print "     l1: ", nums1, " ** n1: ", n1
            #print "     l2: ", nums2, " ** n2: ", n2
        if n1 < 0:
            nums1[:n2+1] = nums2[:n2+1]

