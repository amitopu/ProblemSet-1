def firstNonRepeatingCharacter(string):
	"""
	This function takes a string and find the first character in the string which is non-repeating. This implementation is of O(n) time
	complexity and O(1) space complexity where n is the length of the string and all chars in the string are lowecase that is why only 26
	key value pairs in the hash table which is of O(1) space complexity.

	args:
	--------------
	string (str) : a string of lowercase characters

	output:
	--------------
	index (int): index of first character in the string which is non repeating
	
	"""

	# make a dictionary with each char in string as key and occurrence as value
	charOccurrence = {}
	for char in string:
		charOccurrence[char] = charOccurrence.get(char, 0) + 1
	# iterate through the string and find lowest index which has occurrence 1
	for i in range(len(string)):
		if charOccurrence[string[i]] == 1:
			return i
		
	return -1