# Chapter 3 Stacks and Queues
# 3.5 Sort Stack
# Write a program to sort a stack such that the smallest items are on the top
# You can use an additiona temporary stack, but you may not copy the elements
# into any other data structure (such as an array). The stack supports 
# the following operations: push, pop, peek and isEmpty

import os
from stack import Stack

class sortStack:
	def __init__(self):
		self.stack1 = Stack()
		self.stack2 = Stack()

	def push(self, item):
		flag = True

		while not self.stack2.isEmpty():
			tmp = self.stack2.pop()
			if tmp >= item:
				self.stack1.push(item)
				self.stack1.push(tmp)
				flag = False
			else: self.stack1.push(tmp)

		if flag == True:
			self.stack1.push(item)

		while not self.stack1.isEmpty():
			self.stack2.push(self.stack1.pop())


	def pop(self):
		if self.stack2.isEmpty():
			return

		return self.stack2.pop()

	def isEmpty(self):
		return self.stack2.isEmpty()

	def peek(self):
		if self.stack2.isEmpty():
			return

		return self.stack2.peek()

if __name__=="__main__":
	print("test")
	sstack = sortStack()
	sstack.push(3)
	sstack.push(2)
	sstack.push(5)
	sstack.push(1)
	print(sstack.pop())
	print(sstack.peek())