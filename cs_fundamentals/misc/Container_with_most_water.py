"""
Given n non-negative integers a1, a2, ..., an, where each represents 
a point at coordinate (i, ai). n vertical lines are drawn such that 
the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
which together with x-axis forms a container, such that the container 
contains the most water.

Note: You may not slant the container and n is at least 2.
"""

import numpy as np
from operator import itemgetter

class Solution:

	def __init__(self, data):
		key_list = {}
		for k, v in data:
			if v not in key_list.keys():
				key_list[v] = [(k,v)]
			else:
				key_list[v].append((k,v))
		self.dict = key_list

	def find_max(self):
		max_coords = 0
		max_coords_set = []
		for k, coords in self.dict.items():
			sorted_coords = sorted(coords, key=itemgetter(0))
			first, last = sorted_coords[0], sorted_coords[1]
			volume = first[1]*(last[0]-first[0])
			if volume > max_coords:
				max_coords = volume
				max_coords_set = [first, last]
		return max_coords, max_coords_set

if __name__ == "__main__":

	data = [(4,5),(3,5),(7,4),(1,4),(3,4),(7,7),(1,7)]
	
	s = Solution(data)
	print(s.find_max())
	# print(np.sorted(s.dict[5])) 
