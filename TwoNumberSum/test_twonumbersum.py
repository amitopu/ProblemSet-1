import unittest
from twonumbersum import twoNumberSum, twoNumberSumBetter, twoNumberSumBest

class TestTwoNumberSum(unittest.TestCase):

	def test_output_false(self):
		self.assertFalse(twoNumberSum([2,3,6,4,5,7], 42))

	def test_output_true(self):
		self.assertEqual(twoNumberSum([11, -1, 3, 5, 9, 67], 10), [11, -1])

	def test_output_false_better(self):
		self.assertFalse(twoNumberSumBetter([2,3,6,4,5,7], 42))

	def test_output_true_better(self):
		self.assertTrue(11 in twoNumberSumBetter([11, -1, 3, 5, 9, 67], 10))
		self.assertTrue(-1 in twoNumberSumBetter([11, -1, 3, 5, 9, 67], 10))

	def test_output_false_best(self):
		self.assertFalse(twoNumberSumBest([2,3,6,4,5,7], 42))

	def test_output_true_best(self):
		self.assertEqual(twoNumberSumBest([11, -1, 3, 5, 9, 67], 10), [11, -1])


if __name__ == '__main__':
	unittest.main()

