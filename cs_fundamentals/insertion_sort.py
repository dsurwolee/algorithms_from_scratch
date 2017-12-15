######################################
# Author: Daniel S. Lee
# Date: 12-09-17
# Note: Binary Sorting in Python
######################################

def shift_values(array, key_i, j):
	tmp = array[key_i]
	for pos in range(j, key_i):
		array[pos+1] = array[pos]
	array[j] = tmp
	return array

def insertion_sort(array):
	size = len(array)
	for key_i in range(1, size):
		for j in range(key_i-1,-1,-1):
			if array[j] > array[key_i]: 
				if j == 0:
					array = shift_values(array, key_i, j)
				elif array[j-1] <  array[key_i]:
					array = shift_values(array, key_i, j)
 	return array

print(insertion_sort([1,2,5,4]))
print(insertion_sort([1,2,5,6,4]))

print(insertion_sort([5,4,3,2,2]))

#  5, 4, 3, 2
#  1, 5, 3, 2