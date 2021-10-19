def tournamentWinner(competitions, results):
	'''
	This fuction takes two arrays one of which contains competitions, another array contains results of the competitions
	 and returns a string which is the winning team. This implementation has O(n) space and time complexity.

	args:
	-------------
	competitions (list) : nested array. Each element in the outer most list contains two teams.
						First one is home team and second one is awy team.

	results (list) : contains result of each competition. 0 if away team wins and 1 if home team wins.

	output:
	-------------
	winner (str) : name of the champion of the tournament.

	'''

	# dictionary 'scores' stores all team scores
	scores = {}
	#updating scores of each team by iteration over results and competitions.
	for i in range(len(results)):
		if results[i] == 0:
			if competitions[i][1] in scores:
				scores[competitions[i][1]] += 3
			else:
				scores[competitions[i][1]] = 3
		else:
			if competitions[i][0] in scores:
				scores[competitions[i][0]] += 3
			else:
				scores[competitions[i][0]] = 3
				
	# finding the max scorer from 'scores' dictionary
	max_score = 0
	winner = ''
	for key in scores:
		score = scores[key]
		if score > max_score:
			max_score = score
			winner = str(key)
			
	return winner