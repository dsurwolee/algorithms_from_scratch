######################################
# Author: Daniel S. Lee
# Date: 12-09-17
# Note: Binary Search in Python
######################################
 
def midpoint(array):
	""" Find the midpoint of a binary tree 
	"""

	size = len(array)
	mid_i = int((size / 2))
	mid_p = array[mid_i]
	return mid_p, mid_i


def binary_search(key, array):
	""" Finds key by splitting the array in halves

	Steps:
		1) Find the midpoint, m, of an array 
		2) If key greater than midpoint, update min index to m + 1.
		   Otherwise, update the max index to m - 1.
		3) Continue until midpoint found

	Example:
		binary_search(12, [1,2,3,4,5,6,7,10,12])	
	"""

	while True:
		mid_p, mid_i = midpoint(array)
		print(mid_p, mid_i)
		if mid_p == key:
			print(mid_p, key)
			print("Key found!")
			break
		elif mid_p < key:
			min_i = mid_i + 1
			array = array[mid_i:]
		else:
			array = array[:mid_i]
