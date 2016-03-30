'''
Find the frequency of a number in sorted array
'''

def freq(nums, x):
	if len(nums) == 0:
		return -1
	elif len(nums) == 1:
		if nums[0] == x:
			return 1
		else:
			return -1

	i = first(nums, x, 0, len(nums))
	if i == -1:
		return -1
	j = last(nums, x, i, len(nums))

	return j - i + 1

def first(nums, x, start, end):
	while start <= end:
		mid = (start + end) / 2
		if mid == 0 or (x > nums[mid - 1] and nums[mid] == x):
			return mid
		elif x > nums[mid]:
			start = mid + 1
		else:
			end = mid - 1

	return -1

def last(nums, x, start, end):
	while start <= end:
		mid = (start + end) / 2
		if (mid == (len(nums)-1)) or (x < nums[mid + 1] and nums[mid] == x):
			return mid
		elif x < nums[mid]:
			end = mid - 1
		else:
			start = mid + 1

	return -1

nums = [1,2,2,3,3,3,3]
print freq(nums,3)
