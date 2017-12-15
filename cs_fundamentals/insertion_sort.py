######################################
# Author: Daniel S. Lee
# Date: 12-09-17
# Note: Insertion Sorting in Python
######################################

def swap(array, key_i, j):
	"""Swaps value in an array"""
	temp = array[key_i]
	array[key_i] = array[j] 
	array[j] = temp
	return array

def insertion_sort(array):
	"""For each element staring in i = 0 to i = n + 1,
	   swap with elements to the left occurs until the value 
	   is less than or i = 0. 
	"""
	for key_i in range(1, len(array)):
		for j in range(key_i-1,-1,-1):
			print(key_i, j)
			if array[j] > array[key_i]:
				array = swap(array, key_i, j)
				key_i = key_i - 1
			else:
				break
	return array