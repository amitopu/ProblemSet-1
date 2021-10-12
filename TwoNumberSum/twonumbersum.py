def twoNumberSum(array, targetSum):
	"""
		This function takes an array of numbers and check if there exists any two numbers sum up to a target number.
		This implementation has O(n^2) time complexity and O(1) space complexity.

		args
		---------
		array: an array of numbers
		targetSum: a target number

		output
		---------
		new_array: an array of two numbers which sum up to target number
		False: if there is no such two sumbers which sum up to target number in the input array

	"""
	new_arr = []
	for i in range(0, len(array)-1):
		for j in range(i+1, len(array)):
			if(array[i] + array[j] == targetSum):
				new_arr.append(array[i])
				new_arr.append(array[j])
	if len(new_arr) != 0:
		return new_arr
	else:
		return False
	
	


def twoNumberSumBetter(array, targetSum):
	"""
		This function takes an array of numbers and check if there exists any two numbers sum up to a target number.
		This implementation has O(nlogn) time complexity and O(1) space complexity.

		args
		---------
		array: an array of numbers
		targetSum: a target number

		output
		---------
		new_array: an array of two numbers which sum up to target number
		False: if there is no such two sumbers which sum up to target number in the input array

	"""

	array.sort()

	left = 0
	right = len(array) - 1

	while left < right:
		if array[left] + array[right] == targetSum:
			return [array[left], array[right]]
		elif array[left] + array[right] < targetSum:
			left += 1
		elif array[left] + array[right] > targetSum:
			right -= 1
	return False


def twoNumberSumBest(array, targetSum):
	"""
		This function takes an array of numbers and check if there exists any two numbers sum up to a target number.
		This implementation has O(n) time complexity and O(n) space complexity.

		args
		---------
		array: an array of numbers
		targetSum: a target number

		output
		---------
		new_array: an array of two numbers which sum up to target number
		False: if there is no such two sumbers which sum up to target number in the input array

	"""
	new_arr = {}
	for num in array:
		targetNum = targetSum - num
		if(targetNum in new_arr):
			return [num, targetNum]
		else:
			new_arr[num] = True
	return False