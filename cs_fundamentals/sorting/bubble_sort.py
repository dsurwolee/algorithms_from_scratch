######################################
# Author: Daniel S. Lee
# Date: 12-09-17
# Note: Bubble Sorting in Python
######################################

def swap(array, i, j):
	tmp = array[i]
	array[i] = array[j]
	array[j] = tmp
	return array

def bubble_sort(array):
	nextIteration = True
	while nextIteration:
		nextIteration = False
		for i in range(len(array) - 1):
			j = i + 1
			if array[j] < array[i]:
				array = swap(array, i, j)
				nextIteration = True
	return array


