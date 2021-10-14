
def sortedSquaredArrayNormal(array):
	""" This function takes in a sorted array and return another sorted array 
	which is formed by squared of elements in the input array. O(nlogn) time complexity
	and O(n) space complexity.
	args:
	---------
	array : sorted array with numbers
	
	output:
	---------
	array : which consists of squared of each elements and is sorted.
	"""
	
	square_arr = []
	for elem in array:
		square_arr.append(elem*elem)
		
	square_arr.sort()
	return square_arr


def sortedSquaredArrayBetter(array):
	""" This function takes in a sorted array and return another sorted array 
	which is formed by squared of elements in the input array. O(n) time complexity
	and O(n) space complexity.
	args:
	---------
	array : sorted array with numbers
	
	output:
	---------
	array : which consists of squared of each elements and is sorted.
	"""
	
	big_index = len(array)-1
	small_index = 0
	output_arr = [0 for elem in array]
	
	# elements of bigger indices inserted first in output array
	for idx in range(len(array)-1, -1, -1):
		small_elem = array[small_index]
		big_elem = array[big_index]
		if(abs(small_elem) > abs(big_elem)):
			output_arr[idx] =  small_elem * small_elem
			small_index += 1 # small index is shifted 1 position to right
		else:
			output_arr[idx] = big_elem * big_elem
			big_index -= 1 # big index is shifted 1 position to left 
			
	return output_arr