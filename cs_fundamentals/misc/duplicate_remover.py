"""
Author: Dan Lee
Note: Write a function that removes duplicates in a list.
"""

import numpy as np
from timeit import timeit
from timeit_wrapper import wrapper

def duplicate_remover_list(array):
	new_array = []
	for e in array:
		if e not in new_array:
			new_array.append(e)
	return new_array

def duplicate_remover_enum(array):
	new_array = []
	for i, e in enumerate(array):
		if e not in new_array:
			new_array.append(e)
	return new_array

def duplicate_remover_set(array):
	return list(set(array))

if __name__ == "__main__":

	list_to_test = [[1,2,1,2,1],
					[1,1,1,1,1],
					[1,3,4,5,5],
					[1,1]]

	np.random.seed(123)
	array_to_test = np.random.randint(1,10,10000).tolist()

	for func in [duplicate_remover_set, duplicate_remover_enum, duplicate_remover_list]:
		t = timeit(wrapper(func, array_to_test), number=5000)
		print(t)