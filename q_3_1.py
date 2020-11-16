# Chapter 3 Stacks and Queues
# Interview Questions 3.1

# Describe how you could use a single array
# to implement three(k) stacks

# There are two method - from GeeksforGeeks
# Method 1 - Divide the array in slots of size n/k (Its not efficient use of array space)
# Method 2 - A space efficient implementation

# Need two array to store indexes of each top elements, indexes of next item
# for the items in array arr[]

class KStacks:
	def __init__(self, k, n):
		self.k = k
		self.n = n

		self.arr = [0] * self.n
		self.top = [-1] * self.k

		self.next = [i+1 for i in range(self.n)]
		self.next[self.n - 1] = -1

		self.free = 0

	def isEmpty(self, sn):
		if self.top[sn] == -1:
			return True

	def isFull(self):
		self.free == -1

	def pop(self, sn):
		if self.isEmpty(sn):
			return None

		topVal = self.top[sn]
		self.top[sn] = self.next[self.top[sn]]

		self.next[topVal] = self.free
		self.free = topVal

		return self.arr[topVal]

	def push(self, item, sn):
		if self.isFull():
			print("Stack Overflow")
			return

		indexforinsert = self.free
		self.free = self.next[self.free]

		self.arr[indexforinsert] = item
		self.next[indexforinsert] = self.top[sn]
		self.top[sn] = indexforinsert

	def printstack(self, sn):
		top_index= self.top[sn]
		while(top_index != -1):
			print(self.arr[top_index])
			top_index = self.next[top_index]

if __name__ == "__main__":
	kstacks = KStacks(3, 10) 
	kstacks.push(15, 2)
	kstacks.push(45, 2)
	kstacks.push(17, 1)
	kstacks.push(49, 1)
	kstacks.push(39, 1)
	kstacks.push(11, 0)
	kstacks.push(9, 0)
	kstacks.push(7, 0)

	kstacks.pop(2)
	kstacks.printstack(2)
	kstacks.printstack(1)
	kstacks.printstack(0)




