class QueueEmptyError(Exception):
	def __init__(self):
		super(QueueEmptyError, self).__init__(
			"Empty queue, cannot dequeue item"
		)


class QueueFullError(Exception):
	def __init__(self):
		super(QueueFullError, self).__init__(
			"Queue full, cannot add item to queue"
		)


class Queue(object):

	def __init__(self, max_size=None):
		self.__max_size = max_size
		self.items = []


	def is_empty(self):
		return self.size() == 0


	def size(self):
		return len(self.items)


	def enqueue(self, item):
		if self.size() == self.__max_size:
			raise QueueFullError()

		return self.items.insert(0, item)


	def dequeue(self):
		if self.is_empty():
			raise QueueEmptyError()

		return self.items.pop()
