######################################
# Author: Daniel S. Lee
# Date: 12-09-17
# Note: Peak finding algorithm using binary_search
######################################
 

def peak_finder(a):
	"""Divide and conquer approach to finding a peak
		
	   Finds the peak value in a list of numerical values
	   using the divide and conquer approach. A value is a peak 
	   if it's greater or equal to the values of its neighbors.

	   Pseudocode: 
	       1) If a[mid] >= a[left],
	       	  	reduce list from the mid to last elements
	       2) If a[mid] < a[right],
	       		reduce list from the first to mid-1 elements
		   3) If mid is a peak and mid > mid[right] or mid[left],
		   		mid is a peak 
	
		Worst-case: O(log n)

		Args:
			a: List of integer values

		Returns: 
			a: Reduced list of integer values
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
	