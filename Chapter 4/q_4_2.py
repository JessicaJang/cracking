import unittest
import random
from random import seed
from random import randint
class Node():
	def __init__(self, item, left=None, right=None):
		self.item = item
		self.left = None
		self.right = None

	def disp(self, nesting=0):
		indent = " " * nesting * 2
		output = f"{self.item}\n"
		if self.left is not None:
			output += f"{indent}L:"
			output += self.left.disp(nesting + 1)
		if self.right is not None:
			output += f"{indent}R:"
			output += self.right.disp(nesting + 1)
		return output

	def __str__(self):
		return self.disp()

def minimalTree(array):
	if len(array) == 0: return 
	if len(array) == 1: return Node(array[0])

	mid = len(array) // 2 # index is integer
	# print("array, mid: ", array, mid)
	root = Node(array[mid])

	root.left = minimalTree(array[:mid])
	root.right = minimalTree(array[mid+1:])

	return root

class Test(unittest.TestCase):

	tests = []

	for _ in range(1):
		tests.append(sorted(random.sample(range(0,100), 10)))
		print("tests")

	def test_is_route(self):
		for case in self.tests:
			actual = minimalTree(case)
			print(actual)

if __name__ == "__main__":
    unittest.main()