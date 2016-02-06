class StackEmptyError(Exception):
	def __init__(self):
		super(StackEmptyError, self).__init__("Stack is empty: cannot pop an empty stack")


class StackFullError(Exception):
	def __init__(self):
		super(StackFullError, self).__init__("Stack is full")


class Stack(object):
	def __init__(self, max_size=None):
		self.__max_size = max_size
		self.items = []


	def is_empty(self):
		return self.size() == 0


	def push(self, item):
		if self.size() == self.__max_size:
			raise StackFullError()

		self.items.append(item)


	def pop(self):
		if self.is_empty():
			raise StackEmptyError()

		return self.items.pop()


	def size(self):
		return len(self.items)
