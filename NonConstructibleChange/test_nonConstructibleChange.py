import unittest
from nonConstructibleChange import nonConstructibleChangeBetter, nonConstructibleChangePrimary

class TestNonConstructibleChangePrimary(unittest.TestCase):

	def test_ncc_primary_1(self):
		coins = [1]
		self.assertEqual(nonConstructibleChangePrimary(coins), 2)

	def test_ncc_primary_2(self):
		coins = []
		self.assertEqual(nonConstructibleChangePrimary(coins), 1)

	def test_ncc_primary_3(self):
		coins = [67]
		self.assertEqual(nonConstructibleChangePrimary(coins), 1)

	def test_ncc_primary_4(self):
		coins = [1,2,3,4,5,6,7,8,9,10]
		self.assertEqual(nonConstructibleChangePrimary(coins), 56)

	def test_ncc_primary_5(self):
		coins = [1,1,1,1,1,1]
		self.assertEqual(nonConstructibleChangePrimary(coins), 7)

	def test_ncc_primary_6(self):
		coins = [1, 5, 1, 1, 1, 10, 15, 20, 100]
		self.assertEqual(nonConstructibleChangePrimary(coins), 55)

	def test_ncc_primary_7(self):
		coins = [109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4]
		self.assertEqual(nonConstructibleChangePrimary(coins), 87)


class TestNonConstructibleChangeBetter(unittest.TestCase):

	def test_ncc_better_1(self):
		coins = [1]
		self.assertEqual(nonConstructibleChangeBetter(coins), 2)

	def test_ncc_better_2(self):
		coins = []
		self.assertEqual(nonConstructibleChangeBetter(coins), 1)

	def test_ncc_better_3(self):
		coins = [67]
		self.assertEqual(nonConstructibleChangeBetter(coins), 1)

	def test_ncc_better_4(self):
		coins = [1,2,3,4,5,6,7,8,9,10]
		self.assertEqual(nonConstructibleChangeBetter(coins), 56)

	def test_ncc_better_5(self):
		coins = [1,1,1,1,1,1]
		self.assertEqual(nonConstructibleChangeBetter(coins), 7)

	def test_ncc_better_6(self):
		coins = [1, 5, 1, 1, 1, 10, 15, 20, 100]
		self.assertEqual(nonConstructibleChangeBetter(coins), 55)

	def test_ncc_better_7(self):
		coins = [109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4]
		self.assertEqual(nonConstructibleChangeBetter(coins), 87)