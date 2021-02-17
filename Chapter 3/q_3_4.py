# Chapter 3 Stacks and Queues
# 3.4 Impement a MyQueue class which implements a queue using two stack.

import os
import unittest
from stack import Stack

class MyQueue:
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()

	def isEmpty(self):
		return True if self.stack1.isEmpty() == 0 and self.stack2.isEmpty() == 0 else False

	def add(self, item):
		while not self.stack2.isEmpty():
			self.stack1.push(self.stack2.pop())

		self.stack1.push(item)

	def remove(self):
		while not self.stack1.isEmpty():
			self.stack2.push(self.stack1.pop())

		return self.stack2.pop()

	def peek(self):
		while not self.stack1.isEmpty():
			self.stack2.push(self.stack1.pop())

		return self.stack2.peek()
		
if __name__=="__main__":
	myq = MyQueue()
	myq.add(3)
	myq.add(4)
	myq.add(5)
	assert myq.remove() == 3
	assert myq.peek() == 4
	assert myq.isEmpty() == False




