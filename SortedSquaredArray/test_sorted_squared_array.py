import unittest
from sorted_squared_array import sortedSquaredArrayNormal, sortedSquaredArrayBetter
import random
import time


class TestSortedSquaredArray(unittest.TestCase):

	# Testing of normal algo code

	def test_normal_1(self):
		self.assertEqual(sortedSquaredArrayNormal([1, 2, 3, 5, 6, 8, 9]),[1, 4, 9, 25, 36, 64, 81])
	
	def test_normal_2(self):
		self.assertEqual(sortedSquaredArrayNormal([1]),[1])

	def test_normal_3(self):
		self.assertEqual(sortedSquaredArrayNormal([-1]),[1])

	def test_normal_4(self):
		self.assertEqual(sortedSquaredArrayNormal([-5, -4, -3, -2, -1]),[1, 4, 9, 16, 25])

	def test_normal_5(self):
		self.assertEqual(sortedSquaredArrayNormal([-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]),[0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500])

	def test_normal_6(self):
		self.assertEqual(sortedSquaredArrayNormal([-1, -1, 2, 3, 3, 3, 4]), [1, 1, 4, 9, 9, 9, 16])

	def test_normal_7(self):
		self.assertEqual(sortedSquaredArrayNormal([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

	# Testing of better algo code

	def test_better_1(self):
		self.assertEqual(sortedSquaredArrayBetter([1, 2, 3, 5, 6, 8, 9]),[1, 4, 9, 25, 36, 64, 81])
	
	def test_better_2(self):
		self.assertEqual(sortedSquaredArrayBetter([1]),[1])

	def test_better_3(self):
		self.assertEqual(sortedSquaredArrayBetter([-1]),[1])

	def test_better_4(self):
		self.assertEqual(sortedSquaredArrayBetter([-5, -4, -3, -2, -1]),[1, 4, 9, 16, 25])

	def test_better_5(self):
		self.assertEqual(sortedSquaredArrayBetter([-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]),[0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500])

	def test_betterl_6(self):
		self.assertEqual(sortedSquaredArrayBetter([-1, -1, 2, 3, 3, 3, 4]), [1, 1, 4, 9, 9, 9, 16])

	def test_better_7(self):
		self.assertEqual(sortedSquaredArrayBetter([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

	# Testing runtime comparison

	def test_runtime_compare(self):
		new_arr = [random.randrange(-100, 100) for i in range(100000)]
		new_arr.sort()
		initial = time.time()
		dummy = sortedSquaredArrayNormal(new_arr)
		final  = time.time()
		normal_time = final - initial
		print('Normal time: {}'.format(normal_time))

		time.sleep(5)

		initial = time.time()
		new = sortedSquaredArrayBetter(new_arr)
		final = time.time()
		better_time = final - initial
		print('Better time: {}'.format(better_time))

		self.assertTrue(better_time < normal_time)


