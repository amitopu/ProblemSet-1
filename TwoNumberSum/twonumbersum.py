def twoNumberSum(array, targetSum):
    
    new_array = []
	# iterate over first to n-1 th element as i
	for i in range(0, len(array)-1):
		# iterate over i+1 th to n th element as j
		# check if i th elem + j th elme = 10
		for j in range(i+1, len(array)):
			if(array[i]+array[j] == targetSum):
				new_array.append(array[i])
				new_array.append(array[j])
				
	return new_array

	