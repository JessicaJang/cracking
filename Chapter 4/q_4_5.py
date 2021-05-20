import unittest
import random
from node import Node
from random import seed
from random import randint

def validateBSTminmax(root, minVal=None, maxVal=None):
	if root is None:
		return True

	if (minVal and root.item <= minVal) or (maxVal and root.item > maxVal):
		return False
	if not validateBSTminmax(root.left, minVal, root.item) or not validateBSTminmax(root.right, root.item, maxVal):
		return False

	return True



# def validateBST(root, last_printed):
# 	if root is None:
# 		return True

# 	if not validateBST(root, last_printed): return False

# 	if len(last_printed) and root.item <= last_printed[-1]: 
# 		last_printed = root.item
# 		return False
# 	last_printed[-1] = root.item

# 	if not validateBST(root.right, last_printed): return False

# 	return True

class Test(unittest.TestCase):
	# Case 1
	root = Node(20)
	root.left = Node(10)
	root.right = Node(30)
	# root.left.left = Node(1)
	root.left.right = Node(25)
	# root.right.left = Node(9)

	case1 = root

	tests = [(case1, False)]

	def test_is_route(self):
		print("Number of test: ", len(self.tests))
		for case, res in self.tests:
			# actual = validateBST(case, [])
			actual = validateBSTminmax(case, None, None)
			assert actual == res

if __name__ == "__main__":
    unittest.main()