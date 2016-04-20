'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
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
			print "... nums1: ", nums1[n1], " ..nums2: ", nums2[n2]
			if nums1[n1] >= nums2[n2]:
				nums1[end] = nums1[n1]
				n1 -= 1
			elif nums2[n2] > nums1[n1]:
				nums1[end] = nums2[n2]
				n2 -= 1
			'''
			else:
				nums1[end] = nums1[n1]
				end -= 1
				nums1[end] = nums2[n2]
				n1 -= 1
				n2 -= 1
			'''
			end -= 1
			print "		l1: ", nums1, " ** n1: ", n1
			print "		l2: ", nums2, " ** n2: ", n2
		if n1 < 0:
			nums1[:n2+1] = nums2[:n2+1]
			'''
			while n2 >= 0:
				nums1[end] = nums2[n2]
				end -= 1
				n2 -= 1
			'''
	
s = Solution()
'''
Test1
l1=[1,2,3, None, None, None]
l2=[4,5,6]
'''
'''
Test2
l1 = [1,3,5,7,8,None,None,None]
l2 = [2,4,6]
'''
'''
Test3:
l1 = [12,None,None,None,None]
l2 = [1,3,4,7]
'''
'''
Test4:
l1 = [1,3,4,30,None]
l2 = [2]
'''
'''
Test5
'''
l1 = [0,0,3,0,0,0,0,0,0]
l2 = [-1,1,1,1,2,3]
'''
Test6
l1 = [0]
l2 = [1]
'''
s.merge(l1,3, l2, len(l2))
print l1
