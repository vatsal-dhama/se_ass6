#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from code import modulo

class TestModulo(unittest.TestCase):
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
