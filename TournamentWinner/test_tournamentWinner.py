import unittest
from tournamentWinner import tournamentWinner

class TestTournamentWinner(unittest.TestCase):

	def test_tournament_winner_1(self):
		competetions = [["HTML", "C#"],["C#", "Python"],["Python", "HTML"]]
		results = [0,0,1]
		self.assertEqual(tournamentWinner(competetions, results), 'Python')

	def test_tournament_winner_2(self):
		competetions = [["HTML", "Java"],["Java", "Python"],["Python", "HTML"]]
		results = [0, 1, 1]
		self.assertEqual(tournamentWinner(competetions, results), 'Java')

	def test_tournament_winner_3(self):
		competetions = [["AlgoMasters", "FrontPage Freebirds"],["Runtime Terror", "Static Startup"],["WeC#", "Hypertext Assassins"],
						["AlgoMasters", "WeC#"],["Static Startup", "Hypertext Assassins"],["Runtime Terror", "FrontPage Freebirds"],
    					["AlgoMasters", "Runtime Terror"],["Hypertext Assassins", "FrontPage Freebirds"],["Static Startup", "WeC#"],
						["AlgoMasters", "Static Startup"],["FrontPage Freebirds", "WeC#"],["Hypertext Assassins", "Runtime Terror"],
    					["AlgoMasters", "Hypertext Assassins"],["WeC#", "Runtime Terror"],["FrontPage Freebirds", "Static Startup"]]
		results = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]
		self.assertEqual(tournamentWinner(competetions, results), 'AlgoMasters')