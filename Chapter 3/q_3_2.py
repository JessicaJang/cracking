# Chapter 3 Stacks and Queues
# Interview Questions 3.2

# How would you design a stack which, in addition to push adn pop, 
# has a function min, which returns the minimum element?
# Push, pop and min should all operate in O(1) time

class Stack:
	def __init__(self, n):
		self.arr = []
		self.minVal = 0
		self.n = n

	def isEmpty(self):
		if len(self.arr) == 0:
			return True
		return False

	def isFull(self):
		if self.n == len(self.arr):
			return True
		return False

	def pop(self):
		if self.isEmpty():
			self.minVal = 0
			return None

		tmp = self.arr.pop()
		prev = self.minVal
		if tmp <= self.minVal:
			self.minVal = tmp + self.minVal
			tmp = prev
		
		return tmp


	def push(self, item):
		if self.isEmpty():
			self.minVal = item

		if self.isFull():
			print("Stack is Full")
			return

		if item <= self.minVal:
			tmp = self.minVal
			self.minVal = item
			item = tmp - self.minVal
			
		self.arr.append(item)


	def getMin(self):
		return self.minVal
		
if __name__ == "__main__":
	stack = Stack(10)
	stack.push(3)
	stack.push(5)
	print(stack.getMin())
	stack.push(2)
	stack.push(1)
	print(stack.getMin())
	stack.pop()
	print(stack.getMin())
	stack.pop()
	print(stack.getMin())