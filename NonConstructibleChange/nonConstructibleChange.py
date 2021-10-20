def nonConstructibleChangePrimary(coins):
	"""
		Takes an arrary of coin values and find the minimum change that can't be made by the coins
		available in the array.
		solution complexity : O(nlogn) time complexity and O(1) space complexity
		args:
		-----------
		coins (array): an array contains available coin values.
		
		output:
		-----------
		number (int) : represent the minimum amount of change that can't be made by the coins.
	"""

	# if the array is empty return 1
	# if array has single element and greater than 1 return 1
	n = len(coins)
	if n == 0 or (n == 1 and coins[0] > 1):
		return 1
	#sort the list of coins
	coins.sort()
	# add adjacent elements successively
	# and check if there is a minimum change that can't be done
	sum = 0
	for i in range(len(coins)-1):
		sum += coins[i]
		if coins[i+1] - sum >= 2:
			return sum + 1
	return sum + coins[n-1] + 1



def nonConstructibleChangeBetter(coins):
	"""
		Takes an arrary of coin values and find the minimum change that can't be made by the coins
		available in the array.
		solution complexity : O(nlogn) time complexity and O(1) space complexity and has less lines of code.
		args:
		-----------
		coins (array): an array contains available coin values.
		
		output:
		-----------
		number (int) : represent the minimum amount of change that can't be made by the coins.
	"""

	currentChange = 0
	# sort the array
	coins.sort()
	# iterate through the array and find the minimum change and return
	# if current itaration stage can't find minimum change add current coin 
	# with the current change and make new current change.
	for coin in coins:
		if currentChange + 1 < coin:
			return currentChange + 1
		currentChange += coin
		
	return currentChange + 1