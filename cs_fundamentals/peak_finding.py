######################################
# Author: Daniel S. Lee
# Date: 12-09-17
# Note: Peak finding algorithm using binary_search

# https://codereview.stackexchange.com/questions/145224/1d-peak-finder-algorithm
######################################
 

def peak_finder(a):
	""" Binary split until peak found 
		Worst-case: O(log n)
	"""

	size = len(a)
	mid = (size - 1) // 2
	left = mid - 1
	right = mid + 1

	if size == 1:
		return a
	elif size == 2: 
		if a[mid] >= a[right]:
			return a[mid]
		else: 
			return a[right]
	else:
		if a[mid] >= a[right] and a[mid] >= a[left]:
			return a[mid]
		elif a[mid] >= a[left]:
			return peak_finder(a[mid:])
		else:
			return peak_finder(a[:mid]) 

if __name__ == "__main__":

	array = [1,7,2,3,4,5,6]
	peak = peak_finder(a = array)
	print(array)
	