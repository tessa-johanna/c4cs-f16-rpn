import unittest

import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_substract(self):
		result = rpn.calculate("5 3 -")
		self.assertEqual(2, result)
	def test_multiply(self):
		result = rpn.calculate("5 3 *")
		self.assertEqual(15, result)
	def test_divide(self):
		result = rpn.calculate("6 3 /")
		self.assertEqual(2, result)
	def test_toomanythings(self):
		with self.assertRaises(TypeError):
			rpn.calculate("1 2 3 +")
