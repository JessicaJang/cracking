import unittest
import random
from node import Node
from random import seed
from random import randint
def helper(root, node):
	if root == None: return False
	if root == node: return True

	return helper(root.left, node) or helper(root.right, node)

def ancestorHelper(root, node1, node2):

	if helper(root.left, node1) and helper(root.left, node2):
		return ancestorHelper(root.left, node1, node2)
	if helper(root.right, node1) and helper(root.right, node2):
		return ancestorHelper(root.right, node1, node2)

	return root


def firstCommonAncestor(root, node1, node2):
	# Check if those node1 and node2 are in different side
	if not helper(root, node1) or not helper(root, node2): return None


	return ancestorHelper(root, node1, node2)
	# return None

def firstCommonAncestorOptimized(root, node1, node2):
	if root is None: return None
	if root == node1 and root == node2: return root

	left_side = firstCommonAncestorOptimized(root.left, node1, node2)
	if left_side and left_side != node1 and left_side != node2:
		return left_side

	right_side = firstCommonAncestorOptimized(root.right, node1, node2)
	if right_side and right_side != node1 and right_side != node2:
		return right_side

	# Not one of those cases
	if left_side and right_side: return root
	elif left_side==node1 or right_side==node2: return root
	else: return left_side if left_side else right_side 


# sibling check version

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

	tests = [(root, root.left, root.right, root),
			(root, root.left.right.right, root.left.left, root.left)]

	def test_is_route(self):

		print("Number of test: ", len(self.tests))
		for tree, node1, node2, res in self.tests:
			actual = firstCommonAncestorOptimized(tree, node1, node2)
			assert actual == res

if __name__ == "__main__":
    unittest.main()