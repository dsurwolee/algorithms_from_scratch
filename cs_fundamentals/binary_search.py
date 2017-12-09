######################################
# Author: Daniel S. Lee
# Date: 12-09-17
# Note: Binary Tree in Python
######################################

def midpoint(array):
	""" Find the midpoint of a binary tree 
	"""

	min_i = 0
	max_i = len(array)
	mid_i = (max_i + min_i) / 2 
	if max_i % 2 == 0:   
		mid_r round(mid_i)
		mid_l = mid_r - 1
		mid_pr = array[mid_r] 
		mid_pl = array[mid_l]
		mid_p = (mid_pr + mid_pl) / 2
	else:
		mid_p = array[mid_i]      
	return mid_p, mid_i
 
def binary_search(key, array, _min, _max):
	"""
	"""
	
	mid_p, mid_i = midpoint(array)
	
	if mid_p < key:
		_min = mid_i + 1
	else:
		_max = mid_i - 1

	array = array[_min:_max]
	if len(array) > 1:
		return array[_min:_max]
	else: 
		return mid_i


if __name__ == "__main__":
	array = [2, 4, 6, 7, 10, 12, 15]
	key = 12

	min_i = 0
	max_i = len(array)
	
	cont = True
	while cont:
		array = binary_search(array, key, min_i, min_i)
