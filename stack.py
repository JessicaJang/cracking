class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		if len(self.items) == 0:
			return True
		else:
			return False

	def pop(self):
		return self.items.pop()

	def push(self, item):
		self.items.append(item)

	def peek(self):
		if self.items:
			return self.items[len(self.items) - 1]
		return None

	# def __len__(self):
	# 	return len(self.items)

	# def __bool__(self):
	# 	return bool(self.items)
