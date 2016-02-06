import unittest
import sys

sys.path += ['../']


from queue import (
	Queue,
	QueueEmptyError,
	QueueFullError
)

class TestQueue(unittest.TestCase):

	def setUp(self):
		self.obj = Queue()


	def tearDown(self):
		self.obj = Queue()


	def test_empty_queue(self):
		self.assertTrue(self.obj.is_empty())


	def test_raises_queue_empty_error(self):
		self.assertRaises(QueueEmptyError, lambda: self.obj.dequeue())


	def test_queue_size(self):
		size = 20
		for i in range(size):
			self.obj.enqueue(i)

		self.assertEqual(self.obj.size(), size)


	def test_queue_top_item(self):
		size = 20
		for i in range(size):
			self.obj.enqueue(i)

		self.assertEqual(self.obj.dequeue(), 0)


class TestMaxSizeQueue(unittest.TestCase):

	def setUp(self):
		self.max_size = 10
		self.obj = Queue(max_size=self.max_size)


	def tearDown(self):
		self.obj = Queue(max_size=self.max_size)


	def test_queue_empty(self):
		self.assertTrue(self.obj.is_empty())


	def test_raises_queue_full_error(self):
		for i in range(self.max_size):
			self.obj.enqueue(i)

		self.assertRaises(QueueFullError, lambda: self.obj.enqueue(20))


	def test_queue_top_item(self):
		items = [2, 4, 5, 5]

		for item in items:
			self.obj.enqueue(item)

		self.assertEqual(self.obj.dequeue(), items[0])


if __name__ == '__main__':
	unittest.main()
