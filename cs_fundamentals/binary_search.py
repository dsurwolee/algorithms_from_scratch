######################################
# Author: Daniel S. Lee
# Date: 12-09-17
# Note: Binary Tree in Python
######################################

def midpoint(array):
	""" Find the midpoint of a binary tree 
	"""

	size = len(array)
	if (size % 2) == 0: # Even
		upper_i = int(size / 2)
		lower_i = upper_i - 1
		mid_i   = (upper_i + lower_i) / 2
		mid_p = (array[lower_i] + array[upper_i]) / 2
	else: # Odd
		mid_i = int((size - 1) / 2)
		mid_p = array[mid_i]
	return mid_p, mid_i 
 
# def binary_search(key, array):
# 	""" Finds key by splitting the array in halves

# 	Steps:
# 		1) Find the midpoint, m, of an array 
# 		2) If key greater than midpoint, update min index to m + 1.
# 		   Otherwise, update the max index to m - 1.
# 		3) Continue until midpoint found
# 	"""

# 	min_i, max_i = 0
# 	while True:
# 		mid_p, mid_i = midpoint(array)
	
# 	if mid_p < key:
# 		_min = mid_i + 1
# 	else:
# 		_max = mid_i - 1

# 	array = array[_min:_max]
# 	if len(array) > 1:
# 		return array[_min:_max]
# 	else: 
# 		return mid_i


# if __name__ == "__main__":
# 	array = [2, 4, 6, 7, 10, 12, 15]
# 	key = 12

# 	key_found = binary_search(key=key, array=array)
# 	print(key_found)
