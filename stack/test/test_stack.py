import unittest

import sys
sys.path += ['../']

from stack import (
	Stack,
	StackEmptyError,
	StackFullError
)


class TestStack(unittest.TestCase):

	def setUp(self):
		self.obj = Stack()


	def tearDown(self):
		self.obj = Stack()


	def test_empty_stack(self):
		self.assertTrue(self.obj.is_empty())


	def test_empty_stack_raises_empty_error(self):
		self.assertRaises(StackEmptyError, lambda: self.obj.pop())


	def test_non_empty_stack(self):
		self.obj.push(1)

		self.assertEqual(self.obj.size(), 1)
		self.assertFalse(self.obj.is_empty())
		self.assertEqual(self.obj.pop(), 1)


	def test_push_multiple_items_stack(self):
		nitems = 10
		for i in range(nitems):
			self.obj.push(i)

		self.assertEqual(self.obj.size(), nitems)
		self.assertEqual(self.obj.pop(), nitems-1)


class MaxSizeStack(unittest.TestCase):

	def setUp(self):
		self.max_size = 20
		self.obj = Stack(max_size=self.max_size)

	def tearDown(self):
		self.obj = Stack(max_size=self.max_size)


	def test_empty_stack(self):
		self.assertTrue(self.obj.is_empty())


	def test_raises_stack_full_error(self):
		for i in range(self.max_size):
			self.obj.push(i)

		self.assertEqual(self.obj.size(), self.max_size)
		self.assertRaises(StackFullError, lambda: self.obj.push(12))


if __name__ == '__main__':
	unittest.main()
