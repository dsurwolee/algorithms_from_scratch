"""
Implementation of K-closest points to the origin
"""
from timeit import timeit as tm

def dist(c):
	return sum(v ** 2 for v in c) ** (1 / 2)

# Initial approach
def k_closest_origin(coords):
	return sorted([dist(c), c] for c in coords)[0][1]

# Improved approach 

if __name__ == '__main__':

	data = [(-2, 4),
			( 0,-2),
			(-1, 0),
			( 3, 5),
			(-2, 3),
			( 3, 2)]

	# print(tm("k_closest_origin(data)", setup="from __main__ import k_closest_origin, data"))

	

