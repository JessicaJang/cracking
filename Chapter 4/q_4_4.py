import node
import unittest
import random
from q_4_2 import minimalTree

class BinaryNode:
	def __init__(self, item):
		self.item = item
		self.left = None
		self.right = None

def checkBalance(root):

	# With normal traversal
	if root is None:
		return -1

	# print(root.item)

	left_most_height = checkBalance(root.left)
	if left_most_height >= -1:
		left_height = left_most_height + 1
	else: return -2
	
	right_most_height = checkBalance(root.right)
	if right_most_height >= -1:
		right_height = right_most_height + 1
	else:
		return -2

	print(root.item, "height: ", abs(left_height - right_height))

	if abs(left_height - right_height) > 1:
		return -2
	
	return max(left_height, right_height) # sub-tree height should be max of that sub-tree

class Test(unittest.TestCase):

	tests = []

	for _ in range(1):
		tests.append(random.sample(range(0,100), 10))
		print("Initial: ",tests)

	def test_is_route(self):
		for case in self.tests:
			actual = minimalTree(case)
			level = listofDepths(actual)
			for level_item in level:
				print(level_item)

# This test case is from https://github.com/careercup/CtCI-6th-Edition-Python/blob/0b6b20f79904d54704927d903111c5155d67dc13/chapter_04/p04_check_balanced.py
if __name__ == "__main__":
    # unittest.main()
    root = BinaryNode(1)
    root.left = BinaryNode(2)
    print("Results: ", True if checkBalance(root) >=1 else False)
    root.left.left = BinaryNode(4)
    root.left.right = BinaryNode(5)
    root.left.right.right = BinaryNode(6)
    root.left.right.right.right = BinaryNode(7)
    root.right = BinaryNode(3)
    root.right.left = BinaryNode(8)
    root.right.right = BinaryNode(9)
    root.right.right.right = BinaryNode(10)
    root.right.right.right.right = BinaryNode(11)
    print("Results: ", True if checkBalance(root) >=1 else False)