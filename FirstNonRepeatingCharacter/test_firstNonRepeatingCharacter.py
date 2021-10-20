import unittest
from firstNonRepeatingCharacter import firstNonRepeatingCharacter

class TestFirstNonRepeatingCharacter(unittest.TestCase):

	def test_case_1(self):
		string = 'abcdcaf'
		self.assertEqual(firstNonRepeatingCharacter(string), 1)

	def test_case_2(self):
		string = 'zxjdajfjrhjgjjfhjuhtrsdfbvkjdj'
		self.assertEqual(firstNonRepeatingCharacter(string), 0)

	def test_case_3(self):
		string = 'abchacbhdkdxmh'
		self.assertEqual(firstNonRepeatingCharacter(string), 9)

	def test_case_4(self):
		string = 'aabbccssddffee'
		self.assertEqual(firstNonRepeatingCharacter(string), -1)
