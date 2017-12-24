##############################
# Author: Daniel Lee
# Date: 12-22-17
# Note: Merge Sort 
##############################

from collections import deque

def merge_sort(array=[]):

	def isOdd(size):
		return True if size % 2 != 0 else False
 
	def merge(l,r):
		sorted_list = []
		l, r = [deque(v) for v in [l,r]]
		while True:
			try:
				left_v, right_v = l[0], r[0]
				if left_v <= right_v:
					sorted_list.append(left_v)
					l.popleft()
				else:
					sorted_list.append(right_v)
					r.popleft()
			except:
				not_empty = l if len(l) != 0 else r
				sorted_list.extend(not_empty)
				break
		return sorted_list

	array = [[v] for v in array]
	while True:
		size = len(array)

		if size == 1:
			return array[0]
		else:
			sorted_array = []
			for i in range(size // 2):
				left_array = array[i * 2]
				right_array = array[(i * 2) + 1]
				sorted_array.append(merge(left_array, right_array))
			if isOdd(size): sorted_array.append(array[-1])
			array = sorted_array

 
if __name__ == '__main__':
	
	lists_to_test = [[4,3,2,3,1,1,-43,4,500],
				     [4],
				     [5,5],
				     [6,5]]

	for list_set in lists_to_test:
		print(merge_sort(list_set))
		