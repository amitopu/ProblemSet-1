import unittest
from validate_subsequence import isValidSubsequence

class TestValidateSubsequence(unittest.TestCase):

	def test_first(self):
		self.assertTrue(isValidSubsequence([1,2,3,4,5,6,7,8,9], [4]))

	def test_second(self):
		self.assertTrue(isValidSubsequence([5,8,12,-3,6,89,0,-12], [12, -3, 6, -12]))

	def test_third(self):
		self.assertTrue(isValidSubsequence([2,6,5,7,-1,56,99,-9,90,0,12], [6, 7, -9, 0]))

	def test_fourth(self):
		self.assertFalse(isValidSubsequence([2,6,5,7,-1,56,99,-9,90,0,12], [6, 7, -9, 0, 13]))

	def test_fifth(self):
		self.assertFalse(isValidSubsequence([2,6,5,7,-1,56,99,-9,90,0,12], [-1, 7, 5]))
