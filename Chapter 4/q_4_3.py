import unittest
import random
from linked_list import LinkedList
from q_4_2 import minimalTree

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

def listofDepths(root):
	if root is None: return

	level = []

	queue =[root]
	res = [root.item]
	# make level 0 list
	level.append(LinkedList(res))
	res = []

	cur_count = 1
	child_count = 0

	while queue:
		if cur_count == 0:
			cur_count = child_count
			child_count = 0
			# print(res)
			tmp = LinkedList(res)
			# print(tmp)
			level.append(tmp)
			res = []

		node = queue.pop(0)
		cur_count -= 1

		if node.left:
			child_count += 1
			queue.append(node.left)
			res.append(node.left.item)
		if node.right:
			child_count += 1
			queue.append(node.right)
			res.append(node.right.item)

	return level



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

if __name__ == "__main__":
    unittest.main()