import unittest
import random
from node import Node
from random import seed
from random import randint

# construct parent link of each node
def successor(root):
	if root is None:
		return None

	left_child = successor(root.left)
	if left_child: left_child.parent = root;
	right_child = successor(root.right)
	if right_child: right_child.parent = root;

	return root

# inorder traversal
def find_successor(node):
	if node is None: return None

	# if node does not have right subtree
	if node.right: 
		return left_most(node.right).item
	else:
		q = node.parent
		while q:
			if q.left == node:
				return q.item
			else:
				node = q
				q = node.parent

	return None

def left_most(node):
	if node == None: return None

	while node.left:
		node = node.left
	
	return node

class Test(unittest.TestCase):
	# Case 1
	root = Node(50)
	root.left = Node(30)
	root.right = Node(70)
	root.left.left = Node(10)
	root.left.right = Node(40)
	root.left.right.right = Node(45)

	root.right.left = Node(65)
	root.right.right = Node(90)
	root.right.right.left = Node(85)

	case1 = successor(root)

	root2 = Node(20)
	root2.left = Node(8)
	root2.left.left = Node(4)
	root2.left.right = Node(12)
	root2.left.right.left = Node(10)
	root2.left.right.right = Node(14)
	root2.right = Node(22)

	case2 = successor(root2)

	tests = [(case2, root2.left, 10),
			(case2, root2.left.right.left, 12),
			(case2, root2.left.right.right, 20)]

	def test_is_route(self):

		print("Number of test: ", len(self.tests))
		for tree, case, res in self.tests:
			actual = find_successor(case)
			assert actual == res

if __name__ == "__main__":
    unittest.main()