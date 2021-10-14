def isValidSubsequence(array, sequence):
	"""
		Takes one array and a sequence(another array) and checks if the sequence is the subsequence of the array.
		solution complexity : O(n) time complexity and O(1) space complexity

		args:
		-----------
		array : an array of numbers
		sequence : an array of numbers

		output:
		-----------
		True : if the sequence is subsequence of the array.
		False : if above line is not true.
	"""   
	arr_index = 0
	seq_index = 0
	#iterate over the array and check if elems in sequence are in the array
	while(arr_index <= len(array)-1):
		if(array[arr_index] == sequence[seq_index]):
			if(seq_index == len(sequence)-1):
				return True
			seq_index += 1 # take the next element in the sequence
		arr_index += 1 # take the next elem in the array
	return False