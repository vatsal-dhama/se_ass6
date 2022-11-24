#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from program import modulo

class TestSum(unittest.TestCase):
	def test_1(self):
		a_1 = 1
		b_1 = 2
		result = modulo(a_1, b_1)
		self.assertEqual(result, 1)
		
	def test_2(self):
		a_2 = 2
		b_2 = 2
		result = modulo(a_2, b_2)
		self.assertEqual(result, 0)

	def test_3(self):
		a_3 = 2
		b_3 = 4
		result = modulo(a_3, b_3)
		self.assertEqual(result, 2)

	def test_4(self):
		a_4 = 4
		b_4 = 2
		result = modulo(a_4, b_4)
		self.assertEqual(result, 2) 

	def test_5(self):
		a_5 = 10
		b_5 = 3
		result = modulo(a_5, b_5)
		self.assertEqual(result, 3)

if __name__ == '__main__':
	unittest.main()
