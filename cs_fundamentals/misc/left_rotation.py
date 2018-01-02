""" 
Author: Dan Lee
Note: Left rotation of an array
"""

def left_rotation(d, array=[]): 
	for i in range(d):
		v = array.pop(0)
		array.append(v)
	return array

if __name__ == '__main__':

	# Left rotation:

	# Suppose array = [1,2,3,4,5] Left rotation of d = 2 on 
	# the array would transform the array to [3,4,5,1,2]

	array_to_test = [1,2,3,4,5]
	print(left_rotation(2, array_to_test))

