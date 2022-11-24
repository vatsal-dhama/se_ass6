#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from program import modulo

class TestModulo(unittest.TestCase):
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

if __name__ == '__main__':
	unittest.main()
