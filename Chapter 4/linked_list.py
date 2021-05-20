class LinkedListNode:
	def __init__(self, item, next=None, back=None):
		self.item = item
		self.next = None
		self.back = None

	def __str__(self):
		return str(self.item)


class LinkedList:
	def __init__(self, items=None):
		self.head = None
		self.tail = None

		if items is not None:
			self.add_multiple(items)

	def __iter__(self):
		current = self.head
		while current:
			# yeild can produce a sequence of values,
			# different from return (sends specified value back to its caller)
			yield current
			current = current.next

	def __len__(self):
		length = 0
		node = self.head
		while node:
			length += 1
			node = node.next

		return length

	def __str__(self):
		items = [str(ele) for ele in self]
		return "->".join(items)

	def values(self):
		return [ele.item for ele in self]

	def add(self, item):
		if self.head is None:
			self.tail = self.head = LinkedListNode(item)
		else:
			self.tail.next = LinkedListNode(item)
			self.tail = self.tail.next
		return self.tail

	def add_multiple(self, items):
		for ele in items:
			self.add(ele)

	@classmethod
	def generate(cls, k, min_value, max_value):
		return cls(random.choices(range(min_value, max_value), k=k))
