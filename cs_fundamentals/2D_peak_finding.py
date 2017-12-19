######################################
# Author: Daniel S. Lee
# Date: 12-09-17
# Note: 2D Peak Finder
######################################

import numpy as np

def max(array):
	array = array.tolist()
	chain = [i[0] for i in array]
	m = np.max(chain)
	return [(p, v) for p, v in enumerate(chain) if m == v][0]

def peak_finder(mat):
	"""2D Peak Finder of a N x N Matrix
		
	   Finds the peak in a N x N matrix via divide and conquer
	   approach.

	   Pseudocode: 
	       1) Pick a middle at j = m / 2
	       2) Find a global max at col j at (i, j)
	       3) Compare (i, j - 1), (i, j) and (i, j + 1)
		   4) Pick left if (i, j) > (i, j + 1)
		   		else pick right
		   5) If (i, j) > (i, j - 1), (i, j + 1):
		   		peak found in matrix
		   	
		Complexity: O(nlog(m))

		Args:
			mat: matrix

		Returns: 
			peak value
	"""

	n_size, m_size = mat.shape
	j = m_size // 2
	mid_col = mat[:,j]
	i, max_v = max(mid_col)

	if m_size == 1:
		if n_size == 1: 
			return mat[0,0]
		else:
			return max_v
	elif m_size == 2:
		if mat[i,j - 1] <= mat[i, j]: 
			return max_v
		else:
			return mat[i,j - 1]
	else:
		if mat[i,j - 1] <= mat[i, j]: 
			return peak_finder(mat[:,j:])
		else:
			return peak_finder(mat[:,:j])

if __name__ == "__main__":

	matrix = np.matrix([[1,2,3,4],[4,2,5,4],[15,3,2,1],[16,7,80,10]]) 
	print(peak_finder(matrix))