import unittest
from twonumbersum import twoNumberSum, twoNumberSumBetter

class TestTwoNumberSum(unittest.TestCase):

	def test_output_false(self):
		self.assertFalse(twoNumberSum([2,3,6,4,5,7], 42))

	def test_output_true(self):
		self.assertEqual(twoNumberSum([11, -1, 3, 5, 9, 67], 10), [11, -1])

	def test_output_false_better(self):
		self.assertFalse(twoNumberSum([2,3,6,4,5,7], 42))

	def test_output_true_better(self):
		self.assertEqual(twoNumberSum([11, -1, 3, 5, 9, 67], 10), [11, -1])


if __name__ == '__main__':
	unittest.main()

